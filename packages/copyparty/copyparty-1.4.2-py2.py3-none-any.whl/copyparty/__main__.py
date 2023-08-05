#!/usr/bin/env python3
# coding: utf-8
from __future__ import print_function, unicode_literals

"""copyparty: http file sharing hub (py2/py3)"""
__author__ = "ed <copyparty@ocv.me>"
__copyright__ = 2019
__license__ = "MIT"
__url__ = "https://github.com/9001/copyparty/"

import argparse
import filecmp
import locale
import os
import re
import shutil
import sys
import threading
import time
import traceback
from textwrap import dedent

from .__init__ import ANYWIN, CORES, PY2, VT100, WINDOWS, E, EnvParams, unicode
from .__version__ import CODENAME, S_BUILD_DT, S_VERSION
from .authsrv import re_vol
from .svchub import SvcHub
from .util import (
    IMPLICATIONS,
    JINJA_VER,
    PYFTPD_VER,
    SQLITE_VER,
    align_tab,
    ansi_re,
    min_ex,
    py_desc,
    termsize,
    wrap,
)

try:
    raise Exception()
    raise Exception()

    raise Exception()
except:
    pass

try:
    HAVE_SSL = True
    import ssl
except:
    HAVE_SSL = False

printed  = []


class RiceFormatter(argparse.HelpFormatter):
    def __init__(self, *args , **kwargs )  :
        if PY2:
            kwargs["width"] = termsize()[0]

        super(RiceFormatter, self).__init__(*args, **kwargs)

    def _get_help_string(self, action )  :
        """
        same as ArgumentDefaultsHelpFormatter(HelpFormatter)
        except the help += [...] line now has colors
        """
        fmt = "\033[36m (default: \033[35m%(default)s\033[36m)\033[0m"
        if not VT100:
            fmt = " (default: %(default)s)"

        ret = unicode(action.help)
        if "%(default)" not in ret:
            if action.default is not argparse.SUPPRESS:
                defaulting_nargs = [argparse.OPTIONAL, argparse.ZERO_OR_MORE]
                if action.option_strings or action.nargs in defaulting_nargs:
                    ret += fmt
        return ret

    def _fill_text(self, text , width , indent )  :
        """same as RawDescriptionHelpFormatter(HelpFormatter)"""
        return "".join(indent + line + "\n" for line in text.splitlines())

    def __add_whitespace(self, idx , iWSpace , text )  :
        return (" " * iWSpace) + text if idx else text

    def _split_lines(self, text , width )  :
        # https://stackoverflow.com/a/35925919
        textRows = text.splitlines()
        ptn = re.compile(r"\s*[0-9\-]{0,}\.?\s*")
        for idx, line in enumerate(textRows):
            search = ptn.search(line)
            if not line.strip():
                textRows[idx] = " "
            elif search:
                lWSpace = search.end()
                lines = [
                    self.__add_whitespace(i, lWSpace, x)
                    for i, x in enumerate(wrap(line, width, width - 1))
                ]
                textRows[idx] = lines

        return [item for sublist in textRows for item in sublist]


class Dodge11874(RiceFormatter):
    def __init__(self, *args , **kwargs )  :
        kwargs["width"] = 9003
        super(Dodge11874, self).__init__(*args, **kwargs)


class BasicDodge11874(
    argparse.ArgumentDefaultsHelpFormatter, argparse.RawDescriptionHelpFormatter
):
    def __init__(self, *args , **kwargs )  :
        kwargs["width"] = 9003
        super(BasicDodge11874, self).__init__(*args, **kwargs)


def lprint(*a , **ka )  :
    eol = ka.pop("end", "\n")
    txt  = " ".join(unicode(x) for x in a) + eol
    printed.append(txt)
    if not VT100:
        txt = ansi_re.sub("", txt)

    print(txt, end="", **ka)


def warn(msg )  :
    lprint("\033[1mwarning:\033[0;33m {}\033[0m\n".format(msg))


def init_E(E )  :
    # __init__ runs 18 times when oxidized; do expensive stuff here

    def get_unixdir()  :
        paths    = [
            (os.environ.get, "XDG_CONFIG_HOME"),
            (os.path.expanduser, "~/.config"),
            (os.environ.get, "TMPDIR"),
            (os.environ.get, "TEMP"),
            (os.environ.get, "TMP"),
            (unicode, "/tmp"),
        ]
        for chk in [os.listdir, os.mkdir]:
            for pf, pa in paths:
                try:
                    p = pf(pa)
                    # print(chk.__name__, p, pa)
                    if not p or p.startswith("~"):
                        continue

                    p = os.path.normpath(p)
                    chk(p)  # type: ignore
                    p = os.path.join(p, "copyparty")
                    if not os.path.isdir(p):
                        os.mkdir(p)

                    return p
                except:
                    pass

        raise Exception("could not find a writable path for config")

    def _unpack()  :
        import atexit
        import tarfile
        import tempfile
        from importlib.resources import open_binary

        td = tempfile.TemporaryDirectory(prefix="")
        atexit.register(td.cleanup)
        tdn = td.name

        with open_binary("copyparty", "z.tar") as tgz:
            with tarfile.open(fileobj=tgz) as tf:
                tf.extractall(tdn)

        return tdn

    try:
        E.mod = os.path.dirname(os.path.realpath(__file__))
        if E.mod.endswith("__init__"):
            E.mod = os.path.dirname(E.mod)
    except:
        if not E.ox:
            raise

        E.mod = _unpack()

    if sys.platform == "win32":
        E.cfg = os.path.normpath(os.environ["APPDATA"] + "/copyparty")
    elif sys.platform == "darwin":
        E.cfg = os.path.expanduser("~/Library/Preferences/copyparty")
    else:
        E.cfg = get_unixdir()

    E.cfg = E.cfg.replace("\\", "/")
    try:
        os.makedirs(E.cfg)
    except:
        if not os.path.isdir(E.cfg):
            raise


def ensure_locale()  :
    for x in [
        "en_US.UTF-8",
        "English_United States.UTF8",
        "English_United States.1252",
    ]:
        try:
            locale.setlocale(locale.LC_ALL, x)
            lprint("Locale: {}\n".format(x))
            break
        except:
            continue


def ensure_cert()  :
    """
    the default cert (and the entire TLS support) is only here to enable the
    crypto.subtle javascript API, which is necessary due to the webkit guys
    being massive memers (https://www.chromium.org/blink/webcrypto)

    i feel awful about this and so should they
    """
    cert_insec = os.path.join(E.mod, "res/insecure.pem")
    cert_cfg = os.path.join(E.cfg, "cert.pem")
    if not os.path.exists(cert_cfg):
        shutil.copy(cert_insec, cert_cfg)

    try:
        if filecmp.cmp(cert_cfg, cert_insec):
            lprint(
                "\033[33m  using default TLS certificate; https will be insecure."
                + "\033[36m\n  certificate location: {}\033[0m\n".format(cert_cfg)
            )
    except:
        pass

    # speaking of the default cert,
    # printf 'NO\n.\n.\n.\n.\ncopyparty-insecure\n.\n' | faketime '2000-01-01 00:00:00' openssl req -x509 -sha256 -newkey rsa:2048 -keyout insecure.pem -out insecure.pem -days $((($(printf %d 0x7fffffff)-$(date +%s --date=2000-01-01T00:00:00Z))/(60*60*24))) -nodes && ls -al insecure.pem && openssl x509 -in insecure.pem -text -noout


def configure_ssl_ver(al )  :
    def terse_sslver(txt )  :
        txt = txt.lower()
        for c in ["_", "v", "."]:
            txt = txt.replace(c, "")

        return txt.replace("tls10", "tls1")

    # oh man i love openssl
    # check this out
    # hold my beer
    ptn = re.compile(r"^OP_NO_(TLS|SSL)v")
    sslver = terse_sslver(al.ssl_ver).split(",")
    flags = [k for k in ssl.__dict__ if ptn.match(k)]
    # SSLv2 SSLv3 TLSv1 TLSv1_1 TLSv1_2 TLSv1_3
    if "help" in sslver:
        avail1 = [terse_sslver(x[6:]) for x in flags]
        avail = " ".join(sorted(avail1) + ["all"])
        lprint("\navailable ssl/tls versions:\n  " + avail)
        sys.exit(0)

    al.ssl_flags_en = 0
    al.ssl_flags_de = 0
    for flag in sorted(flags):
        ver = terse_sslver(flag[6:])
        num = getattr(ssl, flag)
        if ver in sslver:
            al.ssl_flags_en |= num
        else:
            al.ssl_flags_de |= num

    if sslver == ["all"]:
        x = al.ssl_flags_en
        al.ssl_flags_en = al.ssl_flags_de
        al.ssl_flags_de = x

    for k in ["ssl_flags_en", "ssl_flags_de"]:
        num = getattr(al, k)
        lprint("{0}: {1:8x} ({1})".format(k, num))

    # think i need that beer now


def configure_ssl_ciphers(al )  :
    ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    if al.ssl_ver:
        ctx.options &= ~al.ssl_flags_en
        ctx.options |= al.ssl_flags_de

    is_help = al.ciphers == "help"

    if al.ciphers and not is_help:
        try:
            ctx.set_ciphers(al.ciphers)
        except:
            lprint("\n\033[1;31mfailed to set ciphers\033[0m\n")

    if not hasattr(ctx, "get_ciphers"):
        lprint("cannot read cipher list: openssl or python too old")
    else:
        ciphers = [x["description"] for x in ctx.get_ciphers()]
        lprint("\n  ".join(["\nenabled ciphers:"] + align_tab(ciphers) + [""]))

    if is_help:
        sys.exit(0)


def args_from_cfg(cfg_path )  :
    ret  = []
    skip = False
    with open(cfg_path, "rb") as f:
        for ln in [x.decode("utf-8").strip() for x in f]:
            if not ln:
                skip = False
                continue

            if ln.startswith("#"):
                continue

            if not ln.startswith("-"):
                continue

            if skip:
                continue

            try:
                ret.extend(ln.split(" ", 1))
            except:
                ret.append(ln)

    return ret


def sighandler(sig  = None, frame  = None)  :
    msg = [""] * 5
    for th in threading.enumerate():
        stk = sys._current_frames()[th.ident]  # type: ignore
        msg.append(str(th))
        msg.extend(traceback.format_stack(stk))

    msg.append("\n")
    print("\n".join(msg))


def disable_quickedit()  :
    import atexit
    import ctypes
    from ctypes import wintypes

    def ecb(ok , fun , args )  :
        if not ok:
            err  = ctypes.get_last_error()  # type: ignore
            if err:
                raise ctypes.WinError(err)  # type: ignore
        return args

    k32 = ctypes.WinDLL(str("kernel32"), use_last_error=True)  # type: ignore
    if PY2:
        wintypes.LPDWORD = ctypes.POINTER(wintypes.DWORD)

    k32.GetStdHandle.errcheck = ecb
    k32.GetConsoleMode.errcheck = ecb
    k32.SetConsoleMode.errcheck = ecb
    k32.GetConsoleMode.argtypes = (wintypes.HANDLE, wintypes.LPDWORD)
    k32.SetConsoleMode.argtypes = (wintypes.HANDLE, wintypes.DWORD)

    def cmode(out , mode  = None)  :
        h = k32.GetStdHandle(-11 if out else -10)
        if mode:
            return k32.SetConsoleMode(h, mode)  # type: ignore

        cmode = wintypes.DWORD()
        k32.GetConsoleMode(h, ctypes.byref(cmode))
        return cmode.value

    # disable quickedit
    mode = orig_in = cmode(False)
    quickedit = 0x40
    extended = 0x80
    mask = quickedit + extended
    if mode & mask != extended:
        atexit.register(cmode, False, orig_in)
        cmode(False, mode & ~mask | extended)

    # enable colors in case the os.system("rem") trick ever stops working
    if VT100:
        mode = orig_out = cmode(True)
        if mode & 4 != 4:
            atexit.register(cmode, True, orig_out)
            cmode(True, mode | 4)


def showlic()  :
    p = os.path.join(E.mod, "res", "COPYING.txt")
    if not os.path.exists(p):
        print("no relevant license info to display")
        return

    with open(p, "rb") as f:
        print(f.read().decode("utf-8", "replace"))


def run_argparse(argv , formatter , retry )  :
    ap = argparse.ArgumentParser(
        formatter_class=formatter,
        prog="copyparty",
        description="http file sharing hub v{} ({})".format(S_VERSION, S_BUILD_DT),
    )

    try:
        fk_salt = unicode(os.path.getmtime(os.path.join(E.cfg, "cert.pem")))
    except:
        fk_salt = "hunter2"

    hcores = min(CORES, 3)  # 4% faster than 4+ on py3.9 @ r5-4500U

    sects = [
        [
            "accounts",
            "accounts and volumes",
            dedent(
                """
            -a takes username:password,
            -v takes src:dst:\033[33mperm\033[0m1:\033[33mperm\033[0m2:\033[33mperm\033[0mN:\033[32mvolflag\033[0m1:\033[32mvolflag\033[0m2:\033[32mvolflag\033[0mN:...
                * "\033[33mperm\033[0m" is "permissions,username1,username2,..."
                * "\033[32mvolflag\033[0m" is config flags to set on this volume

            list of permissions:
              "r" (read):   list folder contents, download files
              "w" (write):  upload files; need "r" to see the uploads
              "m" (move):   move files and folders; need "w" at destination
              "d" (delete): permanently delete files and folders
              "g" (get):    download files, but cannot see folder contents

            too many volflags to list here, see the other sections

            example:\033[35m
              -a ed:hunter2 -v .::r:rw,ed -v ../inc:dump:w:rw,ed:c,nodupe  \033[36m
              mount current directory at "/" with
               * r (read-only) for everyone
               * rw (read+write) for ed
              mount ../inc at "/dump" with
               * w (write-only) for everyone
               * rw (read+write) for ed
               * reject duplicate files  \033[0m

            if no accounts or volumes are configured,
            current folder will be read/write for everyone

            consider the config file for more flexible account/volume management,
            including dynamic reload at runtime (and being more readable w)
            """
            ),
        ],
        [
            "flags",
            "list of volflags",
            dedent(
                """
            volflags are appended to volume definitions, for example,
            to create a write-only volume with the \033[33mnodupe\033[0m and \033[32mnosub\033[0m flags:
              \033[35m-v /mnt/inc:/inc:w\033[33m:c,nodupe\033[32m:c,nosub

            \033[0muploads, general:
              \033[36mnodupe\033[35m rejects existing files (instead of symlinking them)
              \033[36mnosub\033[35m forces all uploads into the top folder of the vfs
              \033[36mmagic$\033[35m enables filetype detection for nameless uploads
              \033[36mgz\033[35m allows server-side gzip of uploads with ?gz (also c,xz)
              \033[36mpk\033[35m forces server-side compression, optional arg: xz,9

            \033[0mupload rules:
              \033[36mmaxn=250,600\033[35m max 250 uploads over 15min
              \033[36mmaxb=1g,300\033[35m max 1 GiB over 5min (suffixes: b, k, m, g)
              \033[36msz=1k-3m\033[35m allow filesizes between 1 KiB and 3MiB
              \033[36mdf=1g\033[35m ensure 1 GiB free disk space

            \033[0mupload rotation:
            (moves all uploads into the specified folder structure)
              \033[36mrotn=100,3\033[35m 3 levels of subfolders with 100 entries in each
              \033[36mrotf=%Y-%m/%d-%H\033[35m date-formatted organizing
              \033[36mlifetime=3600\033[35m uploads are deleted after 1 hour

            \033[0mdatabase, general:
              \033[36me2d\033[35m sets -e2d (all -e2* args can be set using ce2* volflags)
              \033[36md2ts\033[35m disables metadata collection for existing files
              \033[36md2ds\033[35m disables onboot indexing, overrides -e2ds*
              \033[36md2t\033[35m disables metadata collection, overrides -e2t*
              \033[36md2v\033[35m disables file verification, overrides -e2v*
              \033[36md2d\033[35m disables all database stuff, overrides -e2*
              \033[36mhist=/tmp/cdb\033[35m puts thumbnails and indexes at that location
              \033[36mscan=60\033[35m scan for new files every 60sec, same as --re-maxage
              \033[36mnohash=\\.iso$\033[35m skips hashing file contents if path matches *.iso
              \033[36mnoidx=\\.iso$\033[35m fully ignores the contents at paths matching *.iso
              \033[36mnoforget$\033[35m don't forget files when deleted from disk
              \033[36mxdev\033[35m do not descend into other filesystems
              \033[36mxvol\033[35m skip symlinks leaving the volume root

            \033[0mdatabase, audio tags:
            "mte", "mth", "mtp", "mtm" all work the same as -mte, -mth, ...
              \033[36mmtp=.bpm=f,audio-bpm.py\033[35m uses the "audio-bpm.py" program to
                generate ".bpm" tags from uploads (f = overwrite tags)
              \033[36mmtp=ahash,vhash=media-hash.py\033[35m collects two tags at once

            \033[0mthumbnails:
              \033[36mdthumb\033[35m disables all thumbnails
              \033[36mdvthumb\033[35m disables video thumbnails
              \033[36mdathumb\033[35m disables audio thumbnails (spectrograms)
              \033[36mdithumb\033[35m disables image thumbnails

            \033[0mclient and ux:
              \033[36mhtml_head=TXT\033[35m includes TXT in the <head>
              \033[36mrobots\033[35m allows indexing by search engines (default)
              \033[36mnorobots\033[35m kindly asks search engines to leave

            \033[0mothers:
              \033[36mfk=8\033[35m generates per-file accesskeys,
                which will then be required at the "g" permission
            \033[0m"""
            ),
        ],
        [
            "urlform",
            "how to handle url-form POSTs",
            dedent(
                """
            values for --urlform:
              \033[36mstash\033[35m dumps the data to file and returns length + checksum
              \033[36msave,get\033[35m dumps to file and returns the page like a GET
              \033[36mprint,get\033[35m prints the data in the log and returns GET
              (leave out the ",get" to return an error instead)
            """
            ),
        ],
        [
            "ls",
            "volume inspection",
            dedent(
                """
            \033[35m--ls USR,VOL,FLAGS
              \033[36mUSR\033[0m is a user to browse as; * is anonymous, ** is all users
              \033[36mVOL\033[0m is a single volume to scan, default is * (all vols)
              \033[36mFLAG\033[0m is flags;
                \033[36mv\033[0m in addition to realpaths, print usernames and vpaths
                \033[36mln\033[0m only prints symlinks leaving the volume mountpoint
                \033[36mp\033[0m exits 1 if any such symlinks are found
                \033[36mr\033[0m resumes startup after the listing
            examples:
              --ls '**'          # list all files which are possible to read
              --ls '**,*,ln'     # check for dangerous symlinks
              --ls '**,*,ln,p,r' # check, then start normally if safe
            """
            ),
        ],
    ]

    # fmt: off
    u = unicode
    ap2 = ap.add_argument_group('general options')
    ap2.add_argument("-c", metavar="PATH", type=u, action="append", help="add config file")
    ap2.add_argument("-nc", metavar="NUM", type=int, default=64, help="max num clients")
    ap2.add_argument("-j", metavar="CORES", type=int, default=1, help="max num cpu cores, 0=all")
    ap2.add_argument("-a", metavar="ACCT", type=u, action="append", help="add account, USER:PASS; example [ed:wark]")
    ap2.add_argument("-v", metavar="VOL", type=u, action="append", help="add volume, SRC:DST:FLAG; examples [.::r], [/mnt/nas/music:/music:r:aed]")
    ap2.add_argument("-ed", action="store_true", help="enable the ?dots url parameter / client option which allows clients to see dotfiles / hidden files")
    ap2.add_argument("-emp", action="store_true", help="enable markdown plugins -- neat but dangerous, big XSS risk")
    ap2.add_argument("-mcr", metavar="SEC", type=int, default=60, help="md-editor mod-chk rate")
    ap2.add_argument("--urlform", metavar="MODE", type=u, default="print,get", help="how to handle url-form POSTs; see --help-urlform")
    ap2.add_argument("--wintitle", metavar="TXT", type=u, default="cpp @ $pub", help="window title, for example '$ip-10.1.2.' or '$ip-'")
    ap2.add_argument("--license", action="store_true", help="show licenses and exit")
    ap2.add_argument("--version", action="store_true", help="show versions and exit")

    ap2 = ap.add_argument_group('upload options')
    ap2.add_argument("--dotpart", action="store_true", help="dotfile incomplete uploads, hiding them from clients unless -ed")
    ap2.add_argument("--plain-ip", action="store_true", help="when avoiding filename collisions by appending the uploader's ip to the filename: append the plaintext ip instead of salting and hashing the ip")
    ap2.add_argument("--unpost", metavar="SEC", type=int, default=3600*12, help="grace period where uploads can be deleted by the uploader, even without delete permissions; 0=disabled")
    ap2.add_argument("--reg-cap", metavar="N", type=int, default=38400, help="max number of uploads to keep in memory when running without -e2d; roughly 1 MiB RAM per 600")
    ap2.add_argument("--no-fpool", action="store_true", help="disable file-handle pooling -- instead, repeatedly close and reopen files during upload")
    ap2.add_argument("--use-fpool", action="store_true", help="force file-handle pooling, even if copyparty thinks you're better off without -- probably useful on nfs and cow filesystems (zfs, btrfs)")
    ap2.add_argument("--hardlink", action="store_true", help="prefer hardlinks instead of symlinks when possible (within same filesystem)")
    ap2.add_argument("--never-symlink", action="store_true", help="do not fallback to symlinks when a hardlink cannot be made")
    ap2.add_argument("--no-dedup", action="store_true", help="disable symlink/hardlink creation; copy file contents instead")
    ap2.add_argument("--magic", action="store_true", help="enable filetype detection on nameless uploads")
    ap2.add_argument("--df", metavar="GiB", type=float, default=0, help="ensure GiB free disk space by rejecting upload requests")
    ap2.add_argument("--sparse", metavar="MiB", type=int, default=4, help="windows-only: minimum size of incoming uploads through up2k before they are made into sparse files")
    ap2.add_argument("--turbo", metavar="LVL", type=int, default=0, help="configure turbo-mode in up2k client; 0 = off and warn if enabled, 1 = off, 2 = on, 3 = on and disable datecheck")
    ap2.add_argument("--u2sort", metavar="TXT", type=u, default="s", help="upload order; s=smallest-first, n=alphabetical, fs=force-s, fn=force-n -- alphabetical is a bit slower on fiber/LAN but makes it easier to eyeball if everything went fine")
    ap2.add_argument("--write-uplog", action="store_true", help="write POST reports to textfiles in working-directory")

    ap2 = ap.add_argument_group('network options')
    ap2.add_argument("-i", metavar="IP", type=u, default="0.0.0.0", help="ip to bind (comma-sep.)")
    ap2.add_argument("-p", metavar="PORT", type=u, default="3923", help="ports to bind (comma/range)")
    ap2.add_argument("--rproxy", metavar="DEPTH", type=int, default=1, help="which ip to keep; 0 = tcp, 1 = origin (first x-fwd), 2 = cloudflare, 3 = nginx, -1 = closest proxy")
    ap2.add_argument("--s-wr-sz", metavar="B", type=int, default=256*1024, help="socket write size in bytes")
    ap2.add_argument("--s-wr-slp", metavar="SEC", type=float, default=0, help="debug: socket write delay in seconds")
    ap2.add_argument("--rsp-slp", metavar="SEC", type=float, default=0, help="debug: response delay in seconds")

    ap2 = ap.add_argument_group('SSL/TLS options')
    ap2.add_argument("--http-only", action="store_true", help="disable ssl/tls -- force plaintext")
    ap2.add_argument("--https-only", action="store_true", help="disable plaintext -- force tls")
    ap2.add_argument("--ssl-ver", metavar="LIST", type=u, help="set allowed ssl/tls versions; [help] shows available versions; default is what your python version considers safe")
    ap2.add_argument("--ciphers", metavar="LIST", type=u, help="set allowed ssl/tls ciphers; [help] shows available ciphers")
    ap2.add_argument("--ssl-dbg", action="store_true", help="dump some tls info")
    ap2.add_argument("--ssl-log", metavar="PATH", type=u, help="log master secrets for later decryption in wireshark")

    ap2 = ap.add_argument_group('FTP options')
    ap2.add_argument("--ftp", metavar="PORT", type=int, help="enable FTP server on PORT, for example 3921")
    ap2.add_argument("--ftps", metavar="PORT", type=int, help="enable FTPS server on PORT, for example 3990")
    ap2.add_argument("--ftp-dbg", action="store_true", help="enable debug logging")
    ap2.add_argument("--ftp-nat", metavar="ADDR", type=u, help="the NAT address to use for passive connections")
    ap2.add_argument("--ftp-pr", metavar="P-P", type=u, help="the range of TCP ports to use for passive connections, for example 12000-13000")

    ap2 = ap.add_argument_group('opt-outs')
    ap2.add_argument("-nw", action="store_true", help="never write anything to disk (debug/benchmark)")
    ap2.add_argument("--keep-qem", action="store_true", help="do not disable quick-edit-mode on windows (it is disabled to avoid accidental text selection which will deadlock copyparty)")
    ap2.add_argument("--no-del", action="store_true", help="disable delete operations")
    ap2.add_argument("--no-mv", action="store_true", help="disable move/rename operations")
    ap2.add_argument("-nih", action="store_true", help="no info hostname -- don't show in UI")
    ap2.add_argument("-nid", action="store_true", help="no info disk-usage -- don't show in UI")
    ap2.add_argument("--no-zip", action="store_true", help="disable download as zip/tar")
    ap2.add_argument("--no-lifetime", action="store_true", help="disable automatic deletion of uploads after a certain time (lifetime volflag)")

    ap2 = ap.add_argument_group('safety options')
    ap2.add_argument("-s", action="count", default=0, help="increase safety: Disable thumbnails / potentially dangerous software (ffmpeg/pillow/vips), hide partial uploads, avoid crawlers.\n └─Alias of\033[32m --dotpart --no-thumb --no-mtag-ff --no-robots --force-js")
    ap2.add_argument("-ss", action="store_true", help="further increase safety: Prevent js-injection, accidental move/delete, broken symlinks, 404 on 403, ban on excessive 404s.\n └─Alias of\033[32m -s --no-dot-mv --no-dot-ren --unpost=0 --no-del --no-mv --hardlink --vague-403 --ban-404=50,60,1440 -nih")
    ap2.add_argument("-sss", action="store_true", help="further increase safety: Enable logging to disk, scan for dangerous symlinks.\n └─Alias of\033[32m -ss -lo=cpp-%%Y-%%m%%d-%%H%%M%%S.txt.xz --ls=**,*,ln,p,r")
    ap2.add_argument("--ls", metavar="U[,V[,F]]", type=u, help="do a sanity/safety check of all volumes on startup; arguments USER,VOL,FLAGS; example [**,*,ln,p,r]")
    ap2.add_argument("--salt", type=u, default="hunter2", help="up2k file-hash salt; used to generate unpredictable internal identifiers for uploads -- doesn't really matter")
    ap2.add_argument("--fk-salt", metavar="SALT", type=u, default=fk_salt, help="per-file accesskey salt; used to generate unpredictable URLs for hidden files -- this one DOES matter")
    ap2.add_argument("--no-dot-mv", action="store_true", help="disallow moving dotfiles; makes it impossible to move folders containing dotfiles")
    ap2.add_argument("--no-dot-ren", action="store_true", help="disallow renaming dotfiles; makes it impossible to make something a dotfile")
    ap2.add_argument("--no-logues", action="store_true", help="disable rendering .prologue/.epilogue.html into directory listings")
    ap2.add_argument("--no-readme", action="store_true", help="disable rendering readme.md into directory listings")
    ap2.add_argument("--vague-403", action="store_true", help="send 404 instead of 403 (security through ambiguity, very enterprise)")
    ap2.add_argument("--force-js", action="store_true", help="don't send folder listings as HTML, force clients to use the embedded json instead -- slight protection against misbehaving search engines which ignore --no-robots")
    ap2.add_argument("--no-robots", action="store_true", help="adds http and html headers asking search engines to not index anything")
    ap2.add_argument("--logout", metavar="H", type=float, default="8086", help="logout clients after H hours of inactivity (0.0028=10sec, 0.1=6min, 24=day, 168=week, 720=month, 8760=year)")
    ap2.add_argument("--ban-pw", metavar="N,W,B", type=u, default="9,60,1440", help="more than N wrong passwords in W minutes = ban for B minutes (disable with \"no\")")
    ap2.add_argument("--ban-404", metavar="N,W,B", type=u, default="no", help="hitting more than N 404's in W minutes = ban for B minutes (disabled by default since turbo-up2k counts as 404s)")

    ap2 = ap.add_argument_group('shutdown options')
    ap2.add_argument("--ign-ebind", action="store_true", help="continue running even if it's impossible to listen on some of the requested endpoints")
    ap2.add_argument("--ign-ebind-all", action="store_true", help="continue running even if it's impossible to receive connections at all")
    ap2.add_argument("--exit", metavar="WHEN", type=u, default="", help="shutdown after WHEN has finished; for example 'idx' will do volume indexing + metadata analysis")

    ap2 = ap.add_argument_group('logging options')
    ap2.add_argument("-q", action="store_true", help="quiet")
    ap2.add_argument("-lo", metavar="PATH", type=u, help="logfile, example: cpp-%%Y-%%m%%d-%%H%%M%%S.txt.xz")
    ap2.add_argument("--no-voldump", action="store_true", help="do not list volumes and permissions on startup")
    ap2.add_argument("--log-conn", action="store_true", help="debug: print tcp-server msgs")
    ap2.add_argument("--log-htp", action="store_true", help="debug: print http-server threadpool scaling")
    ap2.add_argument("--ihead", metavar="HEADER", type=u, action='append', help="dump incoming header")
    ap2.add_argument("--lf-url", metavar="RE", type=u, default=r"^/\.cpr/|\?th=[wj]$", help="dont log URLs matching")

    ap2 = ap.add_argument_group('admin panel options')
    ap2.add_argument("--no-reload", action="store_true", help="disable ?reload=cfg (reload users/volumes/volflags from config file)")
    ap2.add_argument("--no-rescan", action="store_true", help="disable ?scan (volume reindexing)")
    ap2.add_argument("--no-stack", action="store_true", help="disable ?stack (list all stacks)")

    ap2 = ap.add_argument_group('thumbnail options')
    ap2.add_argument("--no-thumb", action="store_true", help="disable all thumbnails")
    ap2.add_argument("--no-athumb", action="store_true", help="disable audio thumbnails (spectrograms)")
    ap2.add_argument("--no-vthumb", action="store_true", help="disable video thumbnails")
    ap2.add_argument("--th-size", metavar="WxH", default="320x256", help="thumbnail res")
    ap2.add_argument("--th-mt", metavar="CORES", type=int, default=CORES, help="num cpu cores to use for generating thumbnails")
    ap2.add_argument("--th-convt", metavar="SEC", type=int, default=60, help="conversion timeout in seconds")
    ap2.add_argument("--th-no-crop", action="store_true", help="dynamic height; show full image")
    ap2.add_argument("--th-dec", metavar="LIBS", default="vips,pil,ff", help="image decoders, in order of preference")
    ap2.add_argument("--th-no-jpg", action="store_true", help="disable jpg output")
    ap2.add_argument("--th-no-webp", action="store_true", help="disable webp output")
    ap2.add_argument("--th-ff-jpg", action="store_true", help="force jpg output for video thumbs")
    ap2.add_argument("--th-ff-swr", action="store_true", help="use swresample instead of soxr for audio thumbs")
    ap2.add_argument("--th-poke", metavar="SEC", type=int, default=300, help="activity labeling cooldown -- avoids doing keepalive pokes (updating the mtime) on thumbnail folders more often than SEC seconds")
    ap2.add_argument("--th-clean", metavar="SEC", type=int, default=43200, help="cleanup interval; 0=disabled")
    ap2.add_argument("--th-maxage", metavar="SEC", type=int, default=604800, help="max folder age -- folders which haven't been poked for longer than --th-poke seconds will get deleted every --th-clean seconds")
    ap2.add_argument("--th-covers", metavar="N,N", type=u, default="folder.png,folder.jpg,cover.png,cover.jpg", help="folder thumbnails to stat/look for")
    # https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html
    # https://github.com/libvips/libvips
    # ffmpeg -hide_banner -demuxers | awk '/^ D  /{print$2}' | while IFS= read -r x; do ffmpeg -hide_banner -h demuxer=$x; done | grep -E '^Demuxer |extensions:'
    ap2.add_argument("--th-r-pil", metavar="T,T", type=u, default="bmp,dib,gif,icns,ico,jpg,jpeg,jp2,jpx,pcx,png,pbm,pgm,ppm,pnm,sgi,tga,tif,tiff,webp,xbm,dds,xpm,heif,heifs,heic,heics,avif,avifs", help="image formats to decode using pillow")
    ap2.add_argument("--th-r-vips", metavar="T,T", type=u, default="jpg,jpeg,jp2,jpx,jxl,tif,tiff,png,webp,heic,avif,fit,fits,fts,exr,svg,hdr,ppm,pgm,pfm,gif,nii", help="image formats to decode using pyvips")
    ap2.add_argument("--th-r-ffi", metavar="T,T", type=u, default="apng,avif,avifs,bmp,dds,dib,fit,fits,fts,gif,heic,heics,heif,heifs,icns,ico,jp2,jpeg,jpg,jpx,jxl,pbm,pcx,pfm,pgm,png,pnm,ppm,psd,sgi,tga,tif,tiff,webp,xbm,xpm", help="image formats to decode using ffmpeg")
    ap2.add_argument("--th-r-ffv", metavar="T,T", type=u, default="av1,asf,avi,flv,m4v,mkv,mjpeg,mjpg,mpg,mpeg,mpg2,mpeg2,h264,avc,mts,h265,hevc,mov,3gp,mp4,ts,mpegts,nut,ogv,ogm,rm,vob,webm,wmv", help="video formats to decode using ffmpeg")
    ap2.add_argument("--th-r-ffa", metavar="T,T", type=u, default="aac,m4a,ogg,opus,flac,alac,mp3,mp2,ac3,dts,wma,ra,wav,aif,aiff,au,alaw,ulaw,mulaw,amr,gsm,ape,tak,tta,wv,mpc", help="audio formats to decode using ffmpeg")

    ap2 = ap.add_argument_group('transcoding options')
    ap2.add_argument("--no-acode", action="store_true", help="disable audio transcoding")
    ap2.add_argument("--ac-maxage", metavar="SEC", type=int, default=86400, help="delete cached transcode output after SEC seconds")

    ap2 = ap.add_argument_group('general db options')
    ap2.add_argument("-e2d", action="store_true", help="enable up2k database, making files searchable + enables upload deduplocation")
    ap2.add_argument("-e2ds", action="store_true", help="scan writable folders for new files on startup; sets -e2d")
    ap2.add_argument("-e2dsa", action="store_true", help="scans all folders on startup; sets -e2ds")
    ap2.add_argument("-e2v", action="store_true", help="verify file integrity; rehash all files and compare with db")
    ap2.add_argument("-e2vu", action="store_true", help="on hash mismatch: update the database with the new hash")
    ap2.add_argument("-e2vp", action="store_true", help="on hash mismatch: panic and quit copyparty")
    ap2.add_argument("--hist", metavar="PATH", type=u, help="where to store volume data (db, thumbs)")
    ap2.add_argument("--no-hash", metavar="PTN", type=u, help="regex: disable hashing of matching paths during e2ds folder scans")
    ap2.add_argument("--no-idx", metavar="PTN", type=u, help="regex: disable indexing of matching paths during e2ds folder scans")
    ap2.add_argument("--no-dhash", action="store_true", help="disable rescan acceleration; do full database integrity check -- makes the db ~5%% smaller and bootup/rescans 3~10x slower")
    ap2.add_argument("--no-forget", action="store_true", help="never forget indexed files, even when deleted from disk -- makes it impossible to ever upload the same file twice")
    ap2.add_argument("--xdev", action="store_true", help="do not descend into other filesystems (symlink or bind-mount to another HDD, ...)")
    ap2.add_argument("--xvol", action="store_true", help="skip symlinks leaving the volume root")
    ap2.add_argument("--hash-mt", metavar="CORES", type=int, default=hcores, help="num cpu cores to use for file hashing; set 0 or 1 for single-core hashing")
    ap2.add_argument("--re-maxage", metavar="SEC", type=int, default=0, help="disk rescan volume interval, 0=off, can be set per-volume with the 'scan' volflag")
    ap2.add_argument("--db-act", metavar="SEC", type=float, default=10, help="defer any scheduled volume reindexing until SEC seconds after last db write (uploads, renames, ...)")
    ap2.add_argument("--srch-time", metavar="SEC", type=int, default=45, help="search deadline -- terminate searches running for more than SEC seconds")
    ap2.add_argument("--srch-hits", metavar="N", type=int, default=7999, help="max search results to allow clients to fetch; 125 results will be shown initially")

    ap2 = ap.add_argument_group('metadata db options')
    ap2.add_argument("-e2t", action="store_true", help="enable metadata indexing; makes it possible to search for artist/title/codec/resolution/...")
    ap2.add_argument("-e2ts", action="store_true", help="scan existing files on startup; sets -e2t")
    ap2.add_argument("-e2tsr", action="store_true", help="delete all metadata from DB and do a full rescan; sets -e2ts")
    ap2.add_argument("--no-mutagen", action="store_true", help="use FFprobe for tags instead; will catch more tags")
    ap2.add_argument("--no-mtag-ff", action="store_true", help="never use FFprobe as tag reader; is probably safer")
    ap2.add_argument("--mtag-to", metavar="SEC", type=int, default=60, help="timeout for ffprobe tag-scan")
    ap2.add_argument("--mtag-mt", metavar="CORES", type=int, default=CORES, help="num cpu cores to use for tag scanning")
    ap2.add_argument("--mtag-v", action="store_true", help="verbose tag scanning; print errors from mtp subprocesses and such")
    ap2.add_argument("--mtag-vv", action="store_true", help="debug mtp settings")
    ap2.add_argument("-mtm", metavar="M=t,t,t", type=u, action="append", help="add/replace metadata mapping")
    ap2.add_argument("-mte", metavar="M,M,M", type=u, help="tags to index/display (comma-sep.)",
        default="circle,album,.tn,artist,title,.bpm,key,.dur,.q,.vq,.aq,vc,ac,fmt,res,.fps,ahash,vhash")
    ap2.add_argument("-mth", metavar="M,M,M", type=u, help="tags to hide by default (comma-sep.)",
        default=".vq,.aq,vc,ac,fmt,res,.fps")
    ap2.add_argument("-mtp", metavar="M=[f,]BIN", type=u, action="append", help="read tag M using program BIN to parse the file")

    ap2 = ap.add_argument_group('ui options')
    ap2.add_argument("--lang", metavar="LANG", type=u, default="eng", help="language")
    ap2.add_argument("--theme", metavar="NUM", type=int, default=0, help="default theme to use")
    ap2.add_argument("--themes", metavar="NUM", type=int, default=8, help="number of themes installed")
    ap2.add_argument("--favico", metavar="TXT", type=u, default="c 000 none" if retry else "🎉 000 none", help="favicon text [ foreground [ background ] ], set blank to disable")
    ap2.add_argument("--js-browser", metavar="L", type=u, help="URL to additional JS to include")
    ap2.add_argument("--css-browser", metavar="L", type=u, help="URL to additional CSS to include")
    ap2.add_argument("--html-head", metavar="TXT", type=u, default="", help="text to append to the <head> of all HTML pages")
    ap2.add_argument("--textfiles", metavar="CSV", type=u, default="txt,nfo,diz,cue,readme", help="file extensions to present as plaintext")
    ap2.add_argument("--txt-max", metavar="KiB", type=int, default=64, help="max size of embedded textfiles on ?doc= (anything bigger will be lazy-loaded by JS)")
    ap2.add_argument("--doctitle", metavar="TXT", type=u, default="copyparty", help="title / service-name to show in html documents")

    ap2 = ap.add_argument_group('debug options')
    ap2.add_argument("--no-sendfile", action="store_true", help="disable sendfile; instead using a traditional file read loop")
    ap2.add_argument("--no-scandir", action="store_true", help="disable scandir; instead using listdir + stat on each file")
    ap2.add_argument("--no-fastboot", action="store_true", help="wait for up2k indexing before starting the httpd")
    ap2.add_argument("--no-htp", action="store_true", help="disable httpserver threadpool, create threads as-needed instead")
    ap2.add_argument("--stackmon", metavar="P,S", type=u, help="write stacktrace to Path every S second, for example --stackmon=./st/%%Y-%%m/%%d/%%H%%M.xz,60")
    ap2.add_argument("--log-thrs", metavar="SEC", type=float, help="list active threads every SEC")
    ap2.add_argument("--log-fk", metavar="REGEX", type=u, default="", help="log filekey params for files where path matches REGEX; '.' (a single dot) = all files")
    # fmt: on

    ap2 = ap.add_argument_group("help sections")
    for k, h, _ in sects:
        ap2.add_argument("--help-" + k, action="store_true", help=h)

    ret = ap.parse_args(args=argv[1:])
    for k, h, t in sects:
        k2 = "help_" + k.replace("-", "_")
        if vars(ret)[k2]:
            lprint("# {} help page".format(k))
            lprint(t + "\033[0m")
            sys.exit(0)

    return ret


def main(argv  = None)  :
    time.strptime("19970815", "%Y%m%d")  # python#7980
    if WINDOWS:
        os.system("rem")  # enables colors

    init_E(E)
    if argv is None:
        argv = sys.argv

    f = '\033[36mcopyparty v{} "\033[35m{}\033[36m" ({})\n{}\033[0;36m\n   sqlite v{} | jinja2 v{} | pyftpd v{}\n\033[0m'
    f = f.format(
        S_VERSION,
        CODENAME,
        S_BUILD_DT,
        py_desc().replace("[", "\033[1;30m["),
        SQLITE_VER,
        JINJA_VER,
        PYFTPD_VER,
    )
    lprint(f)

    if "--version" in argv:
        sys.exit(0)

    if "--license" in argv:
        showlic()
        sys.exit(0)

    ensure_locale()
    if HAVE_SSL:
        ensure_cert()

    for k, v in zip(argv[1:], argv[2:]):
        if k == "-c":
            supp = args_from_cfg(v)
            argv.extend(supp)

    deprecated   = []
    for dk, nk in deprecated:
        try:
            idx = argv.index(dk)
        except:
            continue

        msg = "\033[1;31mWARNING:\033[0;1m\n  {} \033[0;33mwas replaced with\033[0;1m {} \033[0;33mand will be removed\n\033[0m"
        lprint(msg.format(dk, nk))
        argv[idx] = nk
        time.sleep(2)

    try:
        if len(argv) == 1 and (ANYWIN or not os.geteuid()):
            argv.extend(["-p80,443,3923", "--ign-ebind"])
    except:
        pass

    retry = False
    for fmtr in [RiceFormatter, RiceFormatter, Dodge11874, BasicDodge11874]:
        try:
            al = run_argparse(argv, fmtr, retry)
        except SystemExit:
            raise
        except:
            retry = True
            lprint("\n[ {} ]:\n{}\n".format(fmtr, min_ex()))

    assert al
    al.E = E  # __init__ is not shared when oxidized

    if WINDOWS and not al.keep_qem:
        try:
            disable_quickedit()
        except:
            lprint("\nfailed to disable quick-edit-mode:\n" + min_ex() + "\n")

    if not VT100:
        al.wintitle = ""

    nstrs  = []
    anymod = False
    for ostr in al.v or []:
        m = re_vol.match(ostr)
        if not m:
            # not our problem
            nstrs.append(ostr)
            continue

        src, dst, perms = m.groups()
        na = [src, dst]
        mod = False
        for opt in perms.split(":"):
            if re.match("c[^,]", opt):
                mod = True
                na.append("c," + opt[1:])
            elif re.sub("^[rwmdg]*", "", opt) and "," not in opt:
                mod = True
                perm = opt[0]
                if perm == "a":
                    perm = "rw"
                na.append(perm + "," + opt[1:])
            else:
                na.append(opt)

        nstr = ":".join(na)
        nstrs.append(nstr if mod else ostr)
        if mod:
            msg = "\033[1;31mWARNING:\033[0;1m\n  -v {} \033[0;33mwas replaced with\033[0;1m\n  -v {} \n\033[0m"
            lprint(msg.format(ostr, nstr))
            anymod = True

    if anymod:
        al.v = nstrs
        time.sleep(2)

    # propagate implications
    for k1, k2 in IMPLICATIONS:
        if getattr(al, k1):
            setattr(al, k2, True)

    al.i = al.i.split(",")
    try:
        if "-" in al.p:
            lo, hi = [int(x) for x in al.p.split("-")]
            al.p = list(range(lo, hi + 1))
        else:
            al.p = [int(x) for x in al.p.split(",")]
    except:
        raise Exception("invalid value for -p")

    for arg, kname, okays in [["--u2sort", "u2sort", "s n fs fn"]]:
        val = unicode(getattr(al, kname))
        if val not in okays.split():
            zs = "argument {} cannot be '{}'; try one of these: {}"
            raise Exception(zs.format(arg, val, okays))

    if HAVE_SSL:
        if al.ssl_ver:
            configure_ssl_ver(al)

        if al.ciphers:
            configure_ssl_ciphers(al)
    else:
        warn("ssl module does not exist; cannot enable https")

    if PY2 and WINDOWS and al.e2d:
        warn(
            "windows py2 cannot do unicode filenames with -e2d\n"
            + "  (if you crash with codec errors then that is why)"
        )

    if sys.version_info < (3, 6):
        al.no_scandir = True

    # signal.signal(signal.SIGINT, sighandler)

    SvcHub(al, argv, "".join(printed)).run()


if __name__ == "__main__":
    main()
