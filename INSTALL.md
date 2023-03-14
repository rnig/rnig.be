Microsoft Windows [Version 10.0.19044.2486]
(c) Microsoft Corporation. Alle rechten voorbehouden.

C:\Users\Erwin.Geeraerts>cd distrology

C:\Users\Erwin.Geeraerts\distrology>git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   .gitignore

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        cfg/
        pyvenv.cfg
        src/gui.py
        src/hot.py
        src/hots.py
        src/macro.py
        src/paint.py
        src/ply.py
        src/rec.py
        src/rekenen.py
        src/syn_evt_lst.py
        src/syn_evt_lst2.py

no changes added to commit (use "git add" and/or "git commit -a")

C:\Users\Erwin.Geeraerts\distrology>git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   .gitignore

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        cfg/
        pyvenv.cfg
        src/gui.py
        src/hot.py
        src/hots.py
        src/macro.py
        src/paint.py
        src/ply.py
        src/rec.py
        src/rekenen.py
        src/syn_evt_lst.py
        src/syn_evt_lst2.py

no changes added to commit (use "git add" and/or "git commit -a")

C:\Users\Erwin.Geeraerts\distrology>git add .gitignore

C:\Users\Erwin.Geeraerts\distrology>git add cfg

C:\Users\Erwin.Geeraerts\distrology>git commit -m "Playing with merge conflicts."
[main 51fccbe] Playing with merge conflicts.
 6 files changed, 12 insertions(+), 1 deletion(-)
 create mode 100644 cfg/6.png
 create mode 100644 cfg/7.png
 create mode 100644 cfg/=.png
 create mode 100644 cfg/X.png
 create mode 100644 cfg/hello.html

C:\Users\Erwin.Geeraerts\distrology>git add cfg\hello.html

C:\Users\Erwin.Geeraerts\distrology>git commit -m "Added h1."
[main 2ac0ed3] Added h1.
 1 file changed, 1 insertion(+)

C:\Users\Erwin.Geeraerts\distrology>git push
Enumerating objects: 15, done.
Counting objects: 100% (15/15), done.
Delta compression using up to 8 threads
Compressing objects: 100% (13/13), done.
Writing objects: 100% (13/13), 14.09 KiB | 1.56 MiB/s, done.
Total 13 (delta 3), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (3/3), completed with 1 local object.
To https://github.com/erwinge/distrology.git
   de1c447..2ac0ed3  main -> main

C:\Users\Erwin.Geeraerts\distrology>git commit -m "Added h1."
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   cfg/hello.html

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        pyvenv.cfg
        src/gui.py
        src/hot.py
        src/hots.py
        src/macro.py
        src/paint.py
        src/ply.py
        src/rec.py
        src/rekenen.py
        src/syn_evt_lst.py
        src/syn_evt_lst2.py

no changes added to commit (use "git add" and/or "git commit -a")

C:\Users\Erwin.Geeraerts\distrology>git add cfg\hello.html

C:\Users\Erwin.Geeraerts\distrology>git commit -m "Playing with merge conflicts."
[main d39ad9f] Playing with merge conflicts.
 1 file changed, 1 insertion(+), 1 deletion(-)

C:\Users\Erwin.Geeraerts\distrology>git pull
remote: Enumerating objects: 11, done.
remote: Counting objects: 100% (11/11), done.
remote: Compressing objects: 100% (8/8), done.
remote: Total 8 (delta 4), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (8/8), 1.59 KiB | 14.00 KiB/s, done.
From https://github.com/erwinge/distrology
   2ac0ed3..650f852  main       -> origin/main
Auto-merging cfg/hello.html
CONFLICT (content): Merge conflict in cfg/hello.html
Automatic merge failed; fix conflicts and then commit the result.

C:\Users\Erwin.Geeraerts\distrology>git commit -am "Fix merge conflict."
[main fa518f4] Fix merge conflict.

C:\Users\Erwin.Geeraerts\distrology>git push
Enumerating objects: 11, done.
Counting objects: 100% (11/11), done.
Delta compression using up to 8 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 664 bytes | 332.00 KiB/s, done.
Total 5 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/erwinge/distrology.git
   650f852..fa518f4  main -> main

C:\Users\Erwin.Geeraerts\distrology>git log
commit fa518f41d162cf8e641349fbc253ebf8243e8bab (HEAD -> main, origin/main, origin/HEAD)
Merge: d39ad9f 650f852
Author: Erwin Geeraerts <102787897+erwinge@users.noreply.github.com>
Date:   Mon Mar 13 12:30:31 2023 +0100

    Fix merge conflict.

commit d39ad9f41267cc8f5d4f7b991fa42464911f4863
Author: Erwin Geeraerts <102787897+erwinge@users.noreply.github.com>
Date:   Mon Mar 13 12:29:09 2023 +0100

    Playing with merge conflicts.

commit 650f852517fc92fd1bc56c031ef205e9e10c13c4
Author: erwinge <102787897+erwinge@users.noreply.github.com>
Date:   Mon Mar 13 12:29:00 2023 +0100

    Added some style

commit ef61924443e47237ffe576a7050513d6b183e70b
Author: erwinge <102787897+erwinge@users.noreply.github.com>
Date:   Mon Mar 13 12:27:59 2023 +0100

    Update hello.html

commit 2ac0ed3b5707dacf86d4fdd74297ebae0669e83b
Author: Erwin Geeraerts <102787897+erwinge@users.noreply.github.com>
Date:   Mon Mar 13 12:25:36 2023 +0100


C:\Users\Erwin.Geeraerts\distrology>git branch
* main

C:\Users\Erwin.Geeraerts\distrology>git checkout -b style
Switched to a new branch 'style'

C:\Users\Erwin.Geeraerts\distrology>git branch
  main
* style

C:\Users\Erwin.Geeraerts\distrology>git checkout master
error: pathspec 'master' did not match any file(s) known to git

C:\Users\Erwin.Geeraerts\distrology>git checkout main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.

C:\Users\Erwin.Geeraerts\distrology>git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        pyvenv.cfg
        src/gui.py
        src/hot.py
        src/hots.py
        src/macro.py
        src/paint.py
        src/ply.py
        src/rec.py
        src/rekenen.py
        src/syn_evt_lst.py
        src/syn_evt_lst2.py

nothing added to commit but untracked files present (use "git add" to track)

C:\Users\Erwin.Geeraerts\distrology>git checkout style
Switched to branch 'style'

C:\Users\Erwin.Geeraerts\distrology>git status
On branch style
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        pyvenv.cfg
        src/gui.py
        src/hot.py
        src/hots.py
        src/macro.py
        src/paint.py
        src/ply.py
        src/rec.py
        src/rekenen.py
        src/syn_evt_lst.py
        src/syn_evt_lst2.py

nothing added to commit but untracked files present (use "git add" to track)

C:\Users\Erwin.Geeraerts\distrology>git branch
  main
* style

C:\Users\Erwin.Geeraerts\distrology>cd ..

C:\Users\Erwin.Geeraerts>git clone https://github.com/rnig/rnig.be.git
Cloning into 'rnig.be'...
remote: Repository not found.
fatal: repository 'https://github.com/rnig/rnig.be.git/' not found

C:\Users\Erwin.Geeraerts>git clone https://github.com/rnig/rnig.be.git
Cloning into 'rnig.be'...
remote: Repository not found.
fatal: repository 'https://github.com/rnig/rnig.be.git/' not found

C:\Users\Erwin.Geeraerts>git clone https://github.com/rnig/rnig.be.git
Cloning into 'rnig.be'...
remote: Enumerating objects: 6, done.
remote: Counting objects: 100% (6/6), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 6 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (6/6), done.

C:\Users\Erwin.Geeraerts>cd rnig.be

C:\Users\Erwin.Geeraerts\rnig.be>git add
Nothing specified, nothing added.
hint: Maybe you wanted to say 'git add .'?
hint: Turn this message off by running
hint: "git config advice.addEmptyPathspec false"

C:\Users\Erwin.Geeraerts\rnig.be>dir
 Volume in drive C is Windows
 Volume Serial Number is 4656-A218

 Directory of C:\Users\Erwin.Geeraerts\rnig.be

13/03/2023  14:36    <DIR>          .
13/03/2023  14:36    <DIR>          ..
13/03/2023  14:36               161 index.html
13/03/2023  14:35                 9 README.md
               2 File(s)            170 bytes
               2 Dir(s)  67.628.388.352 bytes free

C:\Users\Erwin.Geeraerts\rnig.be>cat README.md
# rnig.be
C:\Users\Erwin.Geeraerts\rnig.be>git add static

C:\Users\Erwin.Geeraerts\rnig.be>git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   static/index.html

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    index.html


C:\Users\Erwin.Geeraerts\rnig.be>git commit -am "First index.html."
[main 68d3a95] First index.html.
 2 files changed, 10 insertions(+), 1 deletion(-)
 delete mode 100644 index.html
 create mode 100644 static/index.html

C:\Users\Erwin.Geeraerts\rnig.be>git push
remote: Permission to rnig/rnig.be.git denied to erwinge.
fatal: unable to access 'https://github.com/rnig/rnig.be.git/': The requested URL returned error: 403

C:\Users\Erwin.Geeraerts\rnig.be>git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

C:\Users\Erwin.Geeraerts\rnig.be>dir
 Volume in drive C is Windows
 Volume Serial Number is 4656-A218

 Directory of C:\Users\Erwin.Geeraerts\rnig.be

13/03/2023  14:37    <DIR>          .
13/03/2023  14:37    <DIR>          ..
13/03/2023  14:35                 9 README.md
13/03/2023  14:37    <DIR>          static
               1 File(s)              9 bytes
               3 Dir(s)  67.622.985.728 bytes free

C:\Users\Erwin.Geeraerts\rnig.be>git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

C:\Users\Erwin.Geeraerts\rnig.be>dir
 Volume in drive C is Windows
 Volume Serial Number is 4656-A218

 Directory of C:\Users\Erwin.Geeraerts\rnig.be

13/03/2023  14:37    <DIR>          .
13/03/2023  14:37    <DIR>          ..
13/03/2023  14:35                 9 README.md
13/03/2023  14:37    <DIR>          static
               1 File(s)              9 bytes
               3 Dir(s)  67.622.907.904 bytes free

C:\Users\Erwin.Geeraerts\rnig.be>git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

C:\Users\Erwin.Geeraerts\rnig.be>git add static

C:\Users\Erwin.Geeraerts\rnig.be>git add static\index.html

C:\Users\Erwin.Geeraerts\rnig.be>git commit -am "First index.html."
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

C:\Users\Erwin.Geeraerts\rnig.be>git push
remote: Permission to rnig/rnig.be.git denied to erwinge.
fatal: unable to access 'https://github.com/rnig/rnig.be.git/': The requested URL returned error: 403

C:\Users\Erwin.Geeraerts\rnig.be>git branch
* main

C:\Users\Erwin.Geeraerts\rnig.be>git checkout -b demo-1
Switched to a new branch 'demo-1'

C:\Users\Erwin.Geeraerts\rnig.be>git status
On branch demo-1
nothing to commit, working tree clean

C:\Users\Erwin.Geeraerts\rnig.be>git push
fatal: The current branch demo-1 has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin demo-1


C:\Users\Erwin.Geeraerts\rnig.be>dir
 Volume in drive C is Windows
 Volume Serial Number is 4656-A218

 Directory of C:\Users\Erwin.Geeraerts\rnig.be

13/03/2023  14:37    <DIR>          .
13/03/2023  14:37    <DIR>          ..
13/03/2023  14:35                 9 README.md
13/03/2023  14:37    <DIR>          static
               1 File(s)              9 bytes
               3 Dir(s)  67.620.900.864 bytes free

C:\Users\Erwin.Geeraerts\rnig.be>git push --set-upstream origin demo-1
remote: Permission to rnig/rnig.be.git denied to erwinge.
fatal: unable to access 'https://github.com/rnig/rnig.be.git/': The requested URL returned error: 403

C:\Users\Erwin.Geeraerts\rnig.be>git push --set-upstream origin demo-1
remote: Permission to rnig/rnig.be.git denied to erwinge.
fatal: unable to access 'https://github.com/rnig/rnig.be.git/': The requested URL returned error: 403

C:\Users\Erwin.Geeraerts\rnig.be>git push --set-upstream origin demo-1
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 462 bytes | 154.00 KiB/s, done.
Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
remote:
remote: Create a pull request for 'demo-1' on GitHub by visiting:
remote:      https://github.com/rnig/rnig.be/pull/new/demo-1
remote:
To https://github.com/rnig/rnig.be.git
 * [new branch]      demo-1 -> demo-1
branch 'demo-1' set up to track 'origin/demo-1'.

C:\Users\Erwin.Geeraerts\rnig.be>move static docs
        1 dir(s) moved.

C:\Users\Erwin.Geeraerts\rnig.be>dir
 Volume in drive C is Windows
 Volume Serial Number is 4656-A218

 Directory of C:\Users\Erwin.Geeraerts\rnig.be

13/03/2023  14:50    <DIR>          .
13/03/2023  14:50    <DIR>          ..
13/03/2023  14:37    <DIR>          docs
13/03/2023  14:35                 9 README.md
               1 File(s)              9 bytes
               3 Dir(s)  67.658.354.688 bytes free

C:\Users\Erwin.Geeraerts\rnig.be>rm README.md

C:\Users\Erwin.Geeraerts\rnig.be>dir
 Volume in drive C is Windows
 Volume Serial Number is 4656-A218

 Directory of C:\Users\Erwin.Geeraerts\rnig.be

13/03/2023  14:50    <DIR>          .
13/03/2023  14:50    <DIR>          ..
13/03/2023  14:37    <DIR>          docs
               0 File(s)              0 bytes
               3 Dir(s)  67.658.346.496 bytes free

C:\Users\Erwin.Geeraerts\rnig.be>dir docs
 Volume in drive C is Windows
 Volume Serial Number is 4656-A218

 Directory of C:\Users\Erwin.Geeraerts\rnig.be\docs

13/03/2023  14:37    <DIR>          .
13/03/2023  14:37    <DIR>          ..
13/03/2023  14:36               161 index.html
               1 File(s)            161 bytes
               2 Dir(s)  67.658.272.768 bytes free

C:\Users\Erwin.Geeraerts\rnig.be>git push
Everything up-to-date

C:\Users\Erwin.Geeraerts\rnig.be>git status
On branch demo-1
Your branch is up to date with 'origin/demo-1'.

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    README.md
        deleted:    static/index.html

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        docs/

no changes added to commit (use "git add" and/or "git commit -a")

C:\Users\Erwin.Geeraerts\rnig.be>git add docs

C:\Users\Erwin.Geeraerts\rnig.be>git rm README.md
rm 'README.md'

C:\Users\Erwin.Geeraerts\rnig.be>git rm static/index.html
rm 'static/index.html'

C:\Users\Erwin.Geeraerts\rnig.be>git rm static
fatal: pathspec 'static' did not match any files

C:\Users\Erwin.Geeraerts\rnig.be>git status
On branch demo-1
Your branch is up to date with 'origin/demo-1'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        deleted:    README.md
        renamed:    static/index.html -> docs/index.html


C:\Users\Erwin.Geeraerts\rnig.be>git add docs\index.html

C:\Users\Erwin.Geeraerts\rnig.be>git push
Everything up-to-date

C:\Users\Erwin.Geeraerts\rnig.be>git commit -am "Reorganised."
[demo-1 494408d] Reorganised.
 2 files changed, 1 deletion(-)
 delete mode 100644 README.md
 rename {static => docs}/index.html (100%)

C:\Users\Erwin.Geeraerts\rnig.be>git push
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Delta compression using up to 8 threads
Compressing objects: 100% (1/1), done.
Writing objects: 100% (2/2), 249 bytes | 124.00 KiB/s, done.
Total 2 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/rnig/rnig.be.git
   68d3a95..494408d  demo-1 -> demo-1

C:\Users\Erwin.Geeraerts\rnig.be>git status
On branch demo-1
Your branch is up to date with 'origin/demo-1'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        src/

nothing added to commit but untracked files present (use "git add" to track)

C:\Users\Erwin.Geeraerts\rnig.be>git add src

C:\Users\Erwin.Geeraerts\rnig.be>git commit -am "Added some source."
[demo-1 a0650fa] Added some source.
 18 files changed, 140 insertions(+)
 create mode 100644 src/classes.py
 create mode 100644 src/classes.py~
 create mode 100644 src/conditions.py
 create mode 100644 src/conditions.py~
 create mode 100644 src/decorator.py
 create mode 100644 src/decorator.py~
 create mode 100644 src/exceptions.py
 create mode 100644 src/exceptions.py~
 create mode 100644 src/lambda.py
 create mode 100644 src/lambda.py~
 create mode 100644 src/loops.py
 create mode 100644 src/loops.py~
 create mode 100644 src/name.py
 create mode 100644 src/name.py~
 create mode 100644 src/sequences.py
 create mode 100644 src/sequences.py~
 create mode 100644 src/sets.py
 create mode 100644 src/sets.py~

C:\Users\Erwin.Geeraerts\rnig.be>git push
Enumerating objects: 22, done.
Counting objects: 100% (22/22), done.
Delta compression using up to 8 threads
Compressing objects: 100% (14/14), done.
Writing objects: 100% (21/21), 2.29 KiB | 234.00 KiB/s, done.
Total 21 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), done.
To https://github.com/rnig/rnig.be.git
   494408d..a0650fa  demo-1 -> demo-1

C:\Users\Erwin.Geeraerts\rnig.be>cd ..

C:\Users\Erwin.Geeraerts>py -m venv rnig.be

C:\Users\Erwin.Geeraerts>py -m pip install Django
Defaulting to user installation because normal site-packages is not writeable
Collecting Django
  Downloading Django-4.1.7-py3-none-any.whl (8.1 MB)
     ---------------------------------------- 8.1/8.1 MB 22.5 MB/s eta 0:00:00
Collecting tzdata
  Downloading tzdata-2022.7-py2.py3-none-any.whl (340 kB)
     ---------------------------------------- 340.1/340.1 kB 20.6 MB/s eta 0:00:00
Collecting asgiref<4,>=3.5.2
  Downloading asgiref-3.6.0-py3-none-any.whl (23 kB)
Collecting sqlparse>=0.2.2
  Downloading sqlparse-0.4.3-py3-none-any.whl (42 kB)
     ---------------------------------------- 42.8/42.8 kB 2.0 MB/s eta 0:00:00
Installing collected packages: tzdata, sqlparse, asgiref, Django
Successfully installed Django-4.1.7 asgiref-3.6.0 sqlparse-0.4.3 tzdata-2022.7

[notice] A new release of pip is available: 23.0 -> 23.0.1
[notice] To update, run: python.exe -m pip install --upgrade pip

C:\Users\Erwin.Geeraerts>py -m pip uninstall Django
Found existing installation: Django 4.1.7
Uninstalling Django-4.1.7:
  Would remove:
    c:\users\erwin.geeraerts\appdata\roaming\python\python310\scripts\django-admin.exe
    c:\users\erwin.geeraerts\appdata\roaming\python\python310\site-packages\django-4.1.7.dist-info\*
    c:\users\erwin.geeraerts\appdata\roaming\python\python310\site-packages\django\*
Proceed (Y/n)? Y
  Successfully uninstalled Django-4.1.7

C:\Users\Erwin.Geeraerts>rnig.be\Scripts\activate

(rnig.be) C:\Users\Erwin.Geeraerts>cd rnig.be

(rnig.be) C:\Users\Erwin.Geeraerts\rnig.be>py -m pip install Django
Collecting Django
  Using cached Django-4.1.7-py3-none-any.whl (8.1 MB)
Collecting asgiref<4,>=3.5.2
  Using cached asgiref-3.6.0-py3-none-any.whl (23 kB)
Collecting sqlparse>=0.2.2
  Using cached sqlparse-0.4.3-py3-none-any.whl (42 kB)
Collecting tzdata
  Using cached tzdata-2022.7-py2.py3-none-any.whl (340 kB)
Installing collected packages: tzdata, sqlparse, asgiref, Django
Successfully installed Django-4.1.7 asgiref-3.6.0 sqlparse-0.4.3 tzdata-2022.7
WARNING: You are using pip version 22.0.4; however, version 23.0.1 is available.
You should consider upgrading via the 'C:\Users\Erwin.Geeraerts\rnig.be\Scripts\python.exe -m pip install --upgrade pip' command.

(rnig.be) C:\Users\Erwin.Geeraerts\rnig.be>py -m pip install --upgrade pip
Requirement already satisfied: pip in c:\users\erwin.geeraerts\rnig.be\lib\site-packages (22.0.4)
Collecting pip
  Using cached pip-23.0.1-py3-none-any.whl (2.1 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 22.0.4
    Uninstalling pip-22.0.4:
      Successfully uninstalled pip-22.0.4
Successfully installed pip-23.0.1

(rnig.be) C:\Users\Erwin.Geeraerts\rnig.be>
 Volume in drive C is Windows
 Volume Serial Number is 4656-A218

 Directory of C:\Users\Erwin.Geeraerts\rnig.be

14/03/2023  07:00    <DIR>          .
14/03/2023  07:00    <DIR>          ..
13/03/2023  14:37    <DIR>          docs
14/03/2023  06:57    <DIR>          Include
14/03/2023  07:00            21.623 INSTALL.md
14/03/2023  06:57    <DIR>          Lib
14/03/2023  06:57                91 pyvenv.cfg
14/03/2023  07:00    <DIR>          Scripts
13/03/2023  16:36    <DIR>          src
               2 File(s)         21.714 bytes
               7 Dir(s)  67.213.156.352 bytes free

(rnig.be) C:\Users\Erwin.Geeraerts\rnig.be>django-admin startproject tt

(rnig.be) C:\Users\Erwin.Geeraerts\rnig.be>dir tt
 Volume in drive C is Windows
 Volume Serial Number is 4656-A218

 Directory of C:\Users\Erwin.Geeraerts\rnig.be\tt

14/03/2023  07:01    <DIR>          .
14/03/2023  07:01    <DIR>          ..
14/03/2023  07:01               680 manage.py
14/03/2023  07:01    <DIR>          tt
               1 File(s)            680 bytes
               3 Dir(s)  67.218.399.232 bytes free

(rnig.be) C:\Users\Erwin.Geeraerts\rnig.be>dir tt\tt
 Volume in drive C is Windows
 Volume Serial Number is 4656-A218

 Directory of C:\Users\Erwin.Geeraerts\rnig.be\tt\tt

14/03/2023  07:01    <DIR>          .
14/03/2023  07:01    <DIR>          ..
14/03/2023  07:01               397 asgi.py
14/03/2023  07:01             3.332 settings.py
14/03/2023  07:01               765 urls.py
14/03/2023  07:01               397 wsgi.py
14/03/2023  07:01                 0 __init__.py
               5 File(s)          4.891 bytes
               2 Dir(s)  67.218.399.232 bytes free

(rnig.be) C:\Users\Erwin.Geeraerts\rnig.be>dir
 Volume in drive C is Windows
 Volume Serial Number is 4656-A218

 Directory of C:\Users\Erwin.Geeraerts\rnig.be

14/03/2023  07:02    <DIR>          .
14/03/2023  07:02    <DIR>          ..
13/03/2023  14:37    <DIR>          docs
14/03/2023  06:57    <DIR>          Include
14/03/2023  07:02            22.305 INSTALL.md
14/03/2023  07:00            21.623 INSTALL.md~
14/03/2023  06:57    <DIR>          Lib
14/03/2023  06:57                91 pyvenv.cfg
14/03/2023  07:00    <DIR>          Scripts
13/03/2023  16:36    <DIR>          src
14/03/2023  07:01    <DIR>          tt
               3 File(s)         44.019 bytes
               8 Dir(s)  67.218.382.848 bytes free

(rnig.be) C:\Users\Erwin.Geeraerts\rnig.be>cd tt

(rnig.be) C:\Users\Erwin.Geeraerts\rnig.be\tt>py manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
March 14, 2023 - 07:03:53
Django version 4.1.7, using settings 'tt.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

