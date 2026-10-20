import re, subprocess, os, shutil, sys, urllib.request, tarfile, io
BASE='https://packages.termux.dev/apt/termux-main/'
PREFIX='data/data/com.termux/files/usr'
def parse(a):
    d={}
    for blk in open(f'Packages-{a}').read().split('\n\n'):
        f=dict(re.findall(r'^(\S+): (.*)$',blk,re.M))
        if 'Package' in f: d[f['Package']]=f
    return d
def fetch(a, pkgs, dest):
    p=parse(a)
    for n in pkgs:
        fn=p[n]['Filename']; local=f'debs/{a}/'+os.path.basename(fn)
        os.makedirs(f'debs/{a}',exist_ok=True)
        if not os.path.exists(local): urllib.request.urlretrieve(BASE+fn, local)
        w=f'tmp/{a}/{n}'; shutil.rmtree(w,ignore_errors=True); os.makedirs(w)
        subprocess.check_call(['ar','x',os.path.abspath(local)],cwd=w)
        data=[x for x in os.listdir(w) if x.startswith('data.tar')][0]
        subprocess.check_call(['tar','xf',data],cwd=w)
        src=os.path.join(w,PREFIX)
        subprocess.check_call(['cp','-a',src+'/.',dest])
for a in sys.argv[1:]:
    for comp,pkgs in [('jdk17',['openjdk-17','libandroid-shmem','libandroid-spawn','libiconv','libjpeg-turbo','zlib','littlecms','libc++']),
                      ]:
        dest=f'out/{comp}-{a}/usr'; shutil.rmtree(f'out/{comp}-{a}',ignore_errors=True); os.makedirs(dest)
        fetch(a,pkgs,dest)
        print(comp,a,'ok')
