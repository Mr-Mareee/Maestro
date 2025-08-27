\<!doctype html\>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Payloads All The Things, a list of useful payloads and bypasses for Web Application Security">

`<link rel="canonical" href="https://swisskyrepo.github.io/PayloadsAllTheThings/Methodology%20and%20Resources/Linux%20-%20Privilege%20Escalation/">`{=html}

`<link rel="prev" href="../Linux%20-%20Persistence/">`{=html}

`<link rel="next" href="../MSSQL%20Server%20-%20Cheatsheet/">`{=html}

`<link rel="icon" href="../../assets/images/favicon.png">`{=html}
<meta name="generator" content="mkdocs-1.6.1, mkdocs-material-9.6.16">

    <title>Linux - Privilege Escalation - Payloads All The Things</title>
      



      <link rel="stylesheet" href="../../assets/stylesheets/main.7e37652d.min.css">
      
        
        <link rel="stylesheet" href="../../assets/stylesheets/palette.06af60db.min.css">
      
      

<style>
  .social-container {
    float: right;
  }
  </style>

    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,300i,400,400i,700,700i%7CRoboto+Mono:400,400i,700,700i&display=fallback">
        <style>:root{--md-text-font:"Roboto";--md-code-font:"Roboto Mono"}</style>
      


      <link rel="stylesheet" href="../../custom.css">

    <script>__md_scope=new URL("../..",location),__md_hash=e=>[...e].reduce(((e,_)=>(e<<5)-e+_.charCodeAt(0)),0),__md_get=(e,_=localStorage,t=__md_scope)=>JSON.parse(_.getItem(t.pathname+"."+e)),__md_set=(e,_,t=localStorage,a=__md_scope)=>{try{t.setItem(a.pathname+"."+e,JSON.stringify(_))}catch(e){}}</script>

      




        <meta  property="og:type"  content="website" >
      
        <meta  property="og:title"  content="Linux - Privilege Escalation - Payloads All The Things" >
      
        <meta  property="og:description"  content="Payloads All The Things, a list of useful payloads and bypasses for Web Application Security" >
      
        <meta  property="og:image"  content="https://swisskyrepo.github.io/PayloadsAllTheThings/assets/images/social/Methodology and Resources/Linux - Privilege Escalation.png" >
      
        <meta  property="og:image:type"  content="image/png" >
      
        <meta  property="og:image:width"  content="1200" >
      
        <meta  property="og:image:height"  content="630" >
      
        <meta  property="og:url"  content="https://swisskyrepo.github.io/PayloadsAllTheThings/Methodology%20and%20Resources/Linux%20-%20Privilege%20Escalation/" >
      
        <meta  name="twitter:card"  content="summary_large_image" >
      
        <meta  name="twitter:title"  content="Linux - Privilege Escalation - Payloads All The Things" >
      
        <meta  name="twitter:description"  content="Payloads All The Things, a list of useful payloads and bypasses for Web Application Security" >
      
        <meta  name="twitter:image"  content="https://swisskyrepo.github.io/PayloadsAllTheThings/assets/images/social/Methodology and Resources/Linux - Privilege Escalation.png" >
      

</head>
<body dir="ltr" data-md-color-scheme="default" data-md-color-primary="indigo" data-md-color-accent="indigo">
`<input class="md-toggle" data-md-toggle="drawer" type="checkbox" id="__drawer" autocomplete="off">`{=html}
`<input class="md-toggle" data-md-toggle="search" type="checkbox" id="__search" autocomplete="off">`{=html}
`<label class="md-overlay" for="__drawer">`{=html}`</label>`{=html}

::::::::::::: {data-md-component="skip"}
        <a href="#linux-privilege-escalation" class="md-skip">
          Skip to content
        </a>
      
    </div>
    <div data-md-component="announce">
      
    </div>


      

<header class="md-header md-header--shadow" data-md-component="header">
<nav class="md-header__inner md-grid" aria-label="Header">

`<a href="../.." title="Payloads All The Things" class="md-header__button md-logo" aria-label="Payloads All The Things" data-md-component="logo">`{=html}

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
`<path d="M12 8a3 3 0 0 0 3-3 3 3 0 0 0-3-3 3 3 0 0 0-3 3 3 3 0 0 0 3 3m0 3.54C9.64 9.35 6.5 8 3 8v11c3.5 0 6.64 1.35 9 3.54 2.36-2.19 5.5-3.54 9-3.54V8c-3.5 0-6.64 1.35-9 3.54"/>`{=html}
</svg>

`</a>`{=html}
`<label class="md-header__button md-icon" for="__drawer">`{=html}

`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">`{=html}`<path d="M3 6h18v2H3zm0 5h18v2H3zm0 5h18v2H3z"/>`{=html}`</svg>`{=html}
`</label>`{=html}

:::: {.md-header__title data-md-component="header-title"}
      <div class="md-header__ellipsis">
        <div class="md-header__topic">
          <span class="md-ellipsis">
            Payloads All The Things
          </span>
        </div>
        <div class="md-header__topic" data-md-component="header-topic">
          <span class="md-ellipsis">
            
              Linux - Privilege Escalation
            
          </span>
        </div>
      </div>
    </div>

      
        <form class="md-header__option" data-md-component="palette">




    <input class="md-option" data-md-color-media="(prefers-color-scheme: light)" data-md-color-scheme="default" data-md-color-primary="indigo" data-md-color-accent="indigo"  aria-label="Switch to dark mode"  type="radio" name="__palette" id="__palette_0">

      <label class="md-header__button md-icon" title="Switch to dark mode" for="__palette_1" hidden>
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 8a4 4 0 0 0-4 4 4 4 0 0 0 4 4 4 4 0 0 0 4-4 4 4 0 0 0-4-4m0 10a6 6 0 0 1-6-6 6 6 0 0 1 6-6 6 6 0 0 1 6 6 6 6 0 0 1-6 6m8-9.31V4h-4.69L12 .69 8.69 4H4v4.69L.69 12 4 15.31V20h4.69L12 23.31 15.31 20H20v-4.69L23.31 12z"/></svg>
      </label>





    <input class="md-option" data-md-color-media="(prefers-color-scheme: dark)" data-md-color-scheme="slate" data-md-color-primary="indigo" data-md-color-accent="indigo"  aria-label="Switch to light mode"  type="radio" name="__palette" id="__palette_1">

      <label class="md-header__button md-icon" title="Switch to light mode" for="__palette_0" hidden>
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 18c-.89 0-1.74-.2-2.5-.55C11.56 16.5 13 14.42 13 12s-1.44-4.5-3.5-5.45C10.26 6.2 11.11 6 12 6a6 6 0 0 1 6 6 6 6 0 0 1-6 6m8-9.31V4h-4.69L12 .69 8.69 4H4v4.69L.69 12 4 15.31V20h4.69L12 23.31 15.31 20H20v-4.69L23.31 12z"/></svg>
      </label>

</form>

      <script>var palette=__md_get("__palette");if(palette&&palette.color){if("(prefers-color-scheme)"===palette.color.media){var media=matchMedia("(prefers-color-scheme: light)"),input=document.querySelector(media.matches?"[data-md-color-media='(prefers-color-scheme: light)']":"[data-md-color-media='(prefers-color-scheme: dark)']");palette.color.media=input.getAttribute("data-md-color-media"),palette.color.scheme=input.getAttribute("data-md-color-scheme"),palette.color.primary=input.getAttribute("data-md-color-primary"),palette.color.accent=input.getAttribute("data-md-color-accent")}for(var[key,value]of Object.entries(palette.color))document.body.setAttribute("data-md-color-"+key,value)}</script>



      
      
        <label class="md-header__button md-icon" for="__search">
          
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M9.5 3A6.5 6.5 0 0 1 16 9.5c0 1.61-.59 3.09-1.56 4.23l.27.27h.79l5 5-1.5 1.5-5-5v-.79l-.27-.27A6.52 6.52 0 0 1 9.5 16 6.5 6.5 0 0 1 3 9.5 6.5 6.5 0 0 1 9.5 3m0 2C7 5 5 7 5 9.5S7 14 9.5 14 14 12 14 9.5 12 5 9.5 5"/></svg>
        </label>
        <div class="md-search" data-md-component="search" role="dialog">

`<label class="md-search__overlay" for="__search">`{=html}`</label>`{=html}

::: {.md-search__inner role="search"}
    <form class="md-search__form" name="search">
      <input type="text" class="md-search__input" name="query" aria-label="Search" placeholder="Search" autocapitalize="off" autocorrect="off" autocomplete="off" spellcheck="false" data-md-component="search-query" required>
      <label class="md-search__icon md-icon" for="__search">
        
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M9.5 3A6.5 6.5 0 0 1 16 9.5c0 1.61-.59 3.09-1.56 4.23l.27.27h.79l5 5-1.5 1.5-5-5v-.79l-.27-.27A6.52 6.52 0 0 1 9.5 16 6.5 6.5 0 0 1 3 9.5 6.5 6.5 0 0 1 9.5 3m0 2C7 5 5 7 5 9.5S7 14 9.5 14 14 12 14 9.5 12 5 9.5 5"/></svg>
        
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M20 11v2H8l5.5 5.5-1.42 1.42L4.16 12l7.92-7.92L13.5 5.5 8 11z"/></svg>
      </label>
      <nav class="md-search__options" aria-label="Search">
        
          <a href="javascript:void(0)" class="md-search__icon md-icon" title="Share" aria-label="Share" data-clipboard data-clipboard-text="" data-md-component="search-share" tabindex="-1">
            
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M18 16.08c-.76 0-1.44.3-1.96.77L8.91 12.7c.05-.23.09-.46.09-.7s-.04-.47-.09-.7l7.05-4.11c.54.5 1.25.81 2.04.81a3 3 0 0 0 3-3 3 3 0 0 0-3-3 3 3 0 0 0-3 3c0 .24.04.47.09.7L8.04 9.81C7.5 9.31 6.79 9 6 9a3 3 0 0 0-3 3 3 3 0 0 0 3 3c.79 0 1.5-.31 2.04-.81l7.12 4.15c-.05.21-.08.43-.08.66 0 1.61 1.31 2.91 2.92 2.91s2.92-1.3 2.92-2.91A2.92 2.92 0 0 0 18 16.08"/></svg>
          </a>
        
        <button type="reset" class="md-search__icon md-icon" title="Clear" aria-label="Clear" tabindex="-1">
          
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 6.41 17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/></svg>
        </button>
      </nav>
      
        <div class="md-search__suggest" data-md-component="search-suggest"></div>
      
    </form>
    <div class="md-search__output">
      <div class="md-search__scrollwrap" tabindex="0" data-md-scrollfix>
        <div class="md-search-result" data-md-component="search-result">
          <div class="md-search-result__meta">
            Initializing search
          </div>
          <ol class="md-search-result__list" role="presentation"></ol>
        </div>
      </div>
    </div>
:::
::::

::::: md-header__source
        <a href="https://github.com/swisskyrepo/PayloadsAllTheThings/" title="Go to repository" class="md-source" data-md-component="source">

::: {.md-source__icon .md-icon}
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><!--! Font Awesome Free 7.0.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2025 Fonticons, Inc.--><path fill="currentColor" d="M173.9 397.4c0 2-2.3 3.6-5.2 3.6-3.3.3-5.6-1.3-5.6-3.6 0-2 2.3-3.6 5.2-3.6 3-.3 5.6 1.3 5.6 3.6m-31.1-4.5c-.7 2 1.3 4.3 4.3 4.9 2.6 1 5.6 0 6.2-2s-1.3-4.3-4.3-5.2c-2.6-.7-5.5.3-6.2 2.3m44.2-1.7c-2.9.7-4.9 2.6-4.6 4.9.3 2 2.9 3.3 5.9 2.6 2.9-.7 4.9-2.6 4.6-4.6-.3-1.9-3-3.2-5.9-2.9M252.8 8C114.1 8 8 113.3 8 252c0 110.9 69.8 205.8 169.5 239.2 12.8 2.3 17.3-5.6 17.3-12.1 0-6.2-.3-40.4-.3-61.4 0 0-70 15-84.7-29.8 0 0-11.4-29.1-27.8-36.6 0 0-22.9-15.7 1.6-15.4 0 0 24.9 2 38.6 25.8 21.9 38.6 58.6 27.5 72.9 20.9 2.3-16 8.8-27.1 16-33.7-55.9-6.2-112.3-14.3-112.3-110.5 0-27.5 7.6-41.3 23.6-58.9-2.6-6.5-11.1-33.3 2.6-67.9 20.9-6.5 69 27 69 27 20-5.6 41.5-8.5 62.8-8.5s42.8 2.9 62.8 8.5c0 0 48.1-33.6 69-27 13.7 34.7 5.2 61.4 2.6 67.9 16 17.7 25.8 31.5 25.8 58.9 0 96.5-58.9 104.2-114.8 110.5 9.2 7.9 17 22.9 17 46.4 0 33.7-.3 75.4-.3 83.6 0 6.5 4.6 14.4 17.3 12.1C436.2 457.8 504 362.9 504 252 504 113.3 391.5 8 252.8 8M105.2 352.9c-1.3 1-1 3.3.7 5.2 1.6 1.6 3.9 2.3 5.2 1 1.3-1 1-3.3-.7-5.2-1.6-1.6-3.9-2.3-5.2-1m-10.8-8.1c-.7 1.3.3 2.9 2.3 3.9 1.6 1 3.6.7 4.3-.7.7-1.3-.3-2.9-2.3-3.9-2-.6-3.6-.3-4.3.7m32.4 35.6c-1.6 1.3-1 4.3 1.3 6.2 2.3 2.3 5.2 2.6 6.5 1 1.3-1.3.7-4.3-1.3-6.2-2.2-2.3-5.2-2.6-6.5-1m-11.4-14.7c-1.6 1-1.6 3.6 0 5.9s4.3 3.3 5.6 2.3c1.6-1.3 1.6-3.9 0-6.2-1.4-2.3-4-3.3-5.6-2"/></svg>
:::

::: md-source__repository
    GitHub
:::

`</a>`{=html}
:::::

</nav>
</header>

    <div class="md-container" data-md-component="container">
      
      
        
          
        
      
      <main class="md-main" data-md-component="main">
        <div class="md-main__inner md-grid">
          
            
              
              <div class="md-sidebar md-sidebar--primary" data-md-component="sidebar" data-md-type="navigation" >
                <div class="md-sidebar__scrollwrap">
                  <div class="md-sidebar__inner">
                    

<nav class="md-nav md-nav--primary" aria-label="Navigation" data-md-level="0">

`<label class="md-nav__title" for="__drawer">`{=html}
`<a href="../.." title="Payloads All The Things" class="md-nav__button md-logo" aria-label="Payloads All The Things" data-md-component="logo">`{=html}

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
`<path d="M12 8a3 3 0 0 0 3-3 3 3 0 0 0-3-3 3 3 0 0 0-3 3 3 3 0 0 0 3 3m0 3.54C9.64 9.35 6.5 8 3 8v11c3.5 0 6.64 1.35 9 3.54 2.36-2.19 5.5-3.54 9-3.54V8c-3.5 0-6.64 1.35-9 3.54"/>`{=html}
</svg>

`</a>`{=html} Payloads All The Things `</label>`{=html}

::::: md-nav__source
      <a href="https://github.com/swisskyrepo/PayloadsAllTheThings/" title="Go to repository" class="md-source" data-md-component="source">

::: {.md-source__icon .md-icon}
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><!--! Font Awesome Free 7.0.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2025 Fonticons, Inc.--><path fill="currentColor" d="M173.9 397.4c0 2-2.3 3.6-5.2 3.6-3.3.3-5.6-1.3-5.6-3.6 0-2 2.3-3.6 5.2-3.6 3-.3 5.6 1.3 5.6 3.6m-31.1-4.5c-.7 2 1.3 4.3 4.3 4.9 2.6 1 5.6 0 6.2-2s-1.3-4.3-4.3-5.2c-2.6-.7-5.5.3-6.2 2.3m44.2-1.7c-2.9.7-4.9 2.6-4.6 4.9.3 2 2.9 3.3 5.9 2.6 2.9-.7 4.9-2.6 4.6-4.6-.3-1.9-3-3.2-5.9-2.9M252.8 8C114.1 8 8 113.3 8 252c0 110.9 69.8 205.8 169.5 239.2 12.8 2.3 17.3-5.6 17.3-12.1 0-6.2-.3-40.4-.3-61.4 0 0-70 15-84.7-29.8 0 0-11.4-29.1-27.8-36.6 0 0-22.9-15.7 1.6-15.4 0 0 24.9 2 38.6 25.8 21.9 38.6 58.6 27.5 72.9 20.9 2.3-16 8.8-27.1 16-33.7-55.9-6.2-112.3-14.3-112.3-110.5 0-27.5 7.6-41.3 23.6-58.9-2.6-6.5-11.1-33.3 2.6-67.9 20.9-6.5 69 27 69 27 20-5.6 41.5-8.5 62.8-8.5s42.8 2.9 62.8 8.5c0 0 48.1-33.6 69-27 13.7 34.7 5.2 61.4 2.6 67.9 16 17.7 25.8 31.5 25.8 58.9 0 96.5-58.9 104.2-114.8 110.5 9.2 7.9 17 22.9 17 46.4 0 33.7-.3 75.4-.3 83.6 0 6.5 4.6 14.4 17.3 12.1C436.2 457.8 504 362.9 504 252 504 113.3 391.5 8 252.8 8M105.2 352.9c-1.3 1-1 3.3.7 5.2 1.6 1.6 3.9 2.3 5.2 1 1.3-1 1-3.3-.7-5.2-1.6-1.6-3.9-2.3-5.2-1m-10.8-8.1c-.7 1.3.3 2.9 2.3 3.9 1.6 1 3.6.7 4.3-.7.7-1.3-.3-2.9-2.3-3.9-2-.6-3.6-.3-4.3.7m32.4 35.6c-1.6 1.3-1 4.3 1.3 6.2 2.3 2.3 5.2 2.6 6.5 1 1.3-1.3.7-4.3-1.3-6.2-2.2-2.3-5.2-2.6-6.5-1m-11.4-14.7c-1.6 1-1.6 3.6 0 5.9s4.3 3.3 5.6 2.3c1.6-1.3 1.6-3.9 0-6.2-1.4-2.3-4-3.3-5.6-2"/></svg>
:::

::: md-source__repository
    GitHub
:::

`</a>`{=html}
:::::

<ul class="md-nav__list" data-md-scrollfix>
<li class="md-nav__item">

`<a href="../.." class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Payloads All The Things

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../CONTRIBUTING/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} CONTRIBUTING

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../DISCLAIMER/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} DISCLAIMER

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item md-nav__item--nested">

`<input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_4" >`{=html}

    <label class="md-nav__link" for="__nav_4" id="__nav_4_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} API Key Leaks

`</span>`{=html}

      <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_4_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_4">
            <span class="md-nav__icon md-icon"></span>
            API Key Leaks
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../API%20Key%20Leaks/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} API Key and Token Leaks

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../API%20Key%20Leaks/IIS-Machine-Keys/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} IIS Machine Keys

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_5" >
        
          
          <label class="md-nav__link" for="__nav_5" id="__nav_5_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} Account Takeover

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_5_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_5">
            <span class="md-nav__icon md-icon"></span>
            Account Takeover
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../Account%20Takeover/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Account Takeover

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../Account%20Takeover/mfa-bypass/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} MFA Bypasses

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_6" >
        
          
          <label class="md-nav__link" for="__nav_6" id="__nav_6_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} Business Logic Errors

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_6_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_6">
            <span class="md-nav__icon md-icon"></span>
            Business Logic Errors
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../Business%20Logic%20Errors/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Business Logic Errors

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_7" >
        
          
          <label class="md-nav__link" for="__nav_7" id="__nav_7_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} CORS Misconfiguration

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_7_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_7">
            <span class="md-nav__icon md-icon"></span>
            CORS Misconfiguration
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../CORS%20Misconfiguration/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} CORS Misconfiguration

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_8" >
        
          
          <label class="md-nav__link" for="__nav_8" id="__nav_8_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} CRLF Injection

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_8_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_8">
            <span class="md-nav__icon md-icon"></span>
            CRLF Injection
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../CRLF%20Injection/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Carriage Return Line Feed

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_9" >
        
          
          <label class="md-nav__link" for="__nav_9" id="__nav_9_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} CSV Injection

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_9_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_9">
            <span class="md-nav__icon md-icon"></span>
            CSV Injection
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../CSV%20Injection/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} CSV Injection

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_10" >
        
          
          <label class="md-nav__link" for="__nav_10" id="__nav_10_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} CVE Exploits

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_10_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_10">
            <span class="md-nav__icon md-icon"></span>
            CVE Exploits
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../CVE%20Exploits/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Common Vulnerabilities and Exposures

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../CVE%20Exploits/Log4Shell/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} CVE-2021-44228 Log4Shell

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_11" >
        
          
          <label class="md-nav__link" for="__nav_11" id="__nav_11_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} Clickjacking

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_11_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_11">
            <span class="md-nav__icon md-icon"></span>
            Clickjacking
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../Clickjacking/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Clickjacking

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_12" >
        
          
          <label class="md-nav__link" for="__nav_12" id="__nav_12_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} Client Side Path Traversal

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_12_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_12">
            <span class="md-nav__icon md-icon"></span>
            Client Side Path Traversal
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../Client%20Side%20Path%20Traversal/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Client Side Path Traversal

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_13" >
        
          
          <label class="md-nav__link" for="__nav_13" id="__nav_13_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} Command Injection

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_13_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_13">
            <span class="md-nav__icon md-icon"></span>
            Command Injection
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../Command%20Injection/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Command Injection

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_14" >
        
          
          <label class="md-nav__link" for="__nav_14" id="__nav_14_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} Cross Site Request Forgery

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_14_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_14">
            <span class="md-nav__icon md-icon"></span>
            Cross Site Request Forgery
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../Cross-Site%20Request%20Forgery/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Cross-Site Request Forgery

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_15" >
        
          
          <label class="md-nav__link" for="__nav_15" id="__nav_15_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} DNS Rebinding

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_15_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_15">
            <span class="md-nav__icon md-icon"></span>
            DNS Rebinding
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../DNS%20Rebinding/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} DNS Rebinding

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_16" >
        
          
          <label class="md-nav__link" for="__nav_16" id="__nav_16_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} DOM Clobbering

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_16_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_16">
            <span class="md-nav__icon md-icon"></span>
            DOM Clobbering
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../DOM%20Clobbering/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} DOM Clobbering

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_17" >
        
          
          <label class="md-nav__link" for="__nav_17" id="__nav_17_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} Denial of Service

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_17_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_17">
            <span class="md-nav__icon md-icon"></span>
            Denial of Service
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../Denial%20of%20Service/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Denial of Service

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_18" >
        
          
          <label class="md-nav__link" for="__nav_18" id="__nav_18_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} Dependency Confusion

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_18_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_18">
            <span class="md-nav__icon md-icon"></span>
            Dependency Confusion
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../Dependency%20Confusion/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Dependency Confusion

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_19" >
        
          
          <label class="md-nav__link" for="__nav_19" id="__nav_19_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} Directory Traversal

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_19_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_19">
            <span class="md-nav__icon md-icon"></span>
            Directory Traversal
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../Directory%20Traversal/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Directory Traversal

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_20" >
        
          
          <label class="md-nav__link" for="__nav_20" id="__nav_20_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} Encoding Transformations

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_20_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_20">
            <span class="md-nav__icon md-icon"></span>
            Encoding Transformations
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../Encoding%20Transformations/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Encoding and Transformations

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_21" >
        
          
          <label class="md-nav__link" for="__nav_21" id="__nav_21_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} External Variable Modification

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_21_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_21">
            <span class="md-nav__icon md-icon"></span>
            External Variable Modification
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../External%20Variable%20Modification/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} External Variable Modification

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_22" >
        
          
          <label class="md-nav__link" for="__nav_22" id="__nav_22_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} File Inclusion

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_22_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_22">
            <span class="md-nav__icon md-icon"></span>
            File Inclusion
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../File%20Inclusion/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} File Inclusion

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../File%20Inclusion/LFI-to-RCE/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} LFI to RCE

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../File%20Inclusion/Wrappers/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Inclusion Using Wrappers

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_23" >
        
          
          <label class="md-nav__link" for="__nav_23" id="__nav_23_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} Google Web Toolkit

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_23_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_23">
            <span class="md-nav__icon md-icon"></span>
            Google Web Toolkit
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../Google%20Web%20Toolkit/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Google Web Toolkit

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_24" >
        
          
          <label class="md-nav__link" for="__nav_24" id="__nav_24_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} GraphQL Injection

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_24_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_24">
            <span class="md-nav__icon md-icon"></span>
            GraphQL Injection
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../GraphQL%20Injection/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} GraphQL Injection

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_25" >
        
          
          <label class="md-nav__link" for="__nav_25" id="__nav_25_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} HTTP Parameter Pollution

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_25_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_25">
            <span class="md-nav__icon md-icon"></span>
            HTTP Parameter Pollution
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../HTTP%20Parameter%20Pollution/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} HTTP Parameter Pollution

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_26" >
        
          
          <label class="md-nav__link" for="__nav_26" id="__nav_26_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} Headless Browser

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_26_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_26">
            <span class="md-nav__icon md-icon"></span>
            Headless Browser
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../Headless%20Browser/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Headless Browser

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_27" >
        
          
          <label class="md-nav__link" for="__nav_27" id="__nav_27_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} Hidden Parameters

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_27_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_27">
            <span class="md-nav__icon md-icon"></span>
            Hidden Parameters
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../Hidden%20Parameters/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} HTTP Hidden Parameters

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_28" >
        
          
          <label class="md-nav__link" for="__nav_28" id="__nav_28_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} Insecure Deserialization

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_28_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_28">
            <span class="md-nav__icon md-icon"></span>
            Insecure Deserialization
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../Insecure%20Deserialization/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Insecure Deserialization

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../Insecure%20Deserialization/DotNET/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} .NET Deserialization

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../Insecure%20Deserialization/Java/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Java Deserialization

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../Insecure%20Deserialization/Node/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Node Deserialization

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../Insecure%20Deserialization/PHP/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} PHP Deserialization

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../Insecure%20Deserialization/Python/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Python Deserialization

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../Insecure%20Deserialization/Ruby/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Ruby Deserialization

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_29" >
        
          
          <label class="md-nav__link" for="__nav_29" id="__nav_29_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} Insecure Direct Object References

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_29_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_29">
            <span class="md-nav__icon md-icon"></span>
            Insecure Direct Object References
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../Insecure%20Direct%20Object%20References/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Insecure Direct Object References

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_30" >
        
          
          <label class="md-nav__link" for="__nav_30" id="__nav_30_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} Insecure Management Interface

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_30_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_30">
            <span class="md-nav__icon md-icon"></span>
            Insecure Management Interface
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../Insecure%20Management%20Interface/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Insecure Management Interface

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_31" >
        
          
          <label class="md-nav__link" for="__nav_31" id="__nav_31_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} Insecure Randomness

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_31_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_31">
            <span class="md-nav__icon md-icon"></span>
            Insecure Randomness
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../Insecure%20Randomness/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Insecure Randomness

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_32" >
        
          
          <label class="md-nav__link" for="__nav_32" id="__nav_32_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} Insecure Source Code Management

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_32_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_32">
            <span class="md-nav__icon md-icon"></span>
            Insecure Source Code Management
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../Insecure%20Source%20Code%20Management/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Insecure Source Code Management

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../Insecure%20Source%20Code%20Management/Bazaar/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Bazaar

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../Insecure%20Source%20Code%20Management/Git/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Git

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../Insecure%20Source%20Code%20Management/Mercurial/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Mercurial

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../Insecure%20Source%20Code%20Management/Subversion/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Subversion

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_33" >
        
          
          <label class="md-nav__link" for="__nav_33" id="__nav_33_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} JSON Web Token

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_33_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_33">
            <span class="md-nav__icon md-icon"></span>
            JSON Web Token
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../JSON%20Web%20Token/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} JWT - JSON Web Token

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_34" >
        
          
          <label class="md-nav__link" for="__nav_34" id="__nav_34_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} Java RMI

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_34_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_34">
            <span class="md-nav__icon md-icon"></span>
            Java RMI
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../Java%20RMI/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Java RMI

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_35" >
        
          
          <label class="md-nav__link" for="__nav_35" id="__nav_35_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} LDAP Injection

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_35_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_35">
            <span class="md-nav__icon md-icon"></span>
            LDAP Injection
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../LDAP%20Injection/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} LDAP Injection

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_36" >
        
          
          <label class="md-nav__link" for="__nav_36" id="__nav_36_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} LaTeX Injection

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_36_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_36">
            <span class="md-nav__icon md-icon"></span>
            LaTeX Injection
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../LaTeX%20Injection/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} LaTeX Injection

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_37" >
        
          
          <label class="md-nav__link" for="__nav_37" id="__nav_37_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} Mass Assignment

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_37_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_37">
            <span class="md-nav__icon md-icon"></span>
            Mass Assignment
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../Mass%20Assignment/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Mass Assignment

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>
















    <li class="md-nav__item md-nav__item--active md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_38" checked>
        
          
          <label class="md-nav__link" for="__nav_38" id="__nav_38_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} Methodology and Resources

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_38_label" aria-expanded="true">
          <label class="md-nav__title" for="__nav_38">
            <span class="md-nav__icon md-icon"></span>
            Methodology and Resources
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../Active%20Directory%20Attack/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Active Directory Attacks

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../Bind%20Shell%20Cheatsheet/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Bind Shell

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../Cloud%20-%20AWS%20Pentest/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Cloud - AWS

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../Cloud%20-%20Azure%20Pentest/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Cloud - Azure

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../Cobalt%20Strike%20-%20Cheatsheet/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Cobalt Strike

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../Container%20-%20Docker%20Pentest/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Container - Docker

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../Container%20-%20Kubernetes%20Pentest/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Container - Kubernetes

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../Escape%20Breakout/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Application Escape and Breakout

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../HTML%20Smuggling/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} HTML Smuggling

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../Hash%20Cracking/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Hash Cracking

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../Initial%20Access/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Initial Access

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../Linux%20-%20Evasion/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Linux - Evasion

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../Linux%20-%20Persistence/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Linux - Persistence

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item md-nav__item--active">

`<input class="md-nav__toggle md-toggle" type="checkbox" id="__toc">`{=html}

`<a href="./" class="md-nav__link md-nav__link--active">`{=html}

`<span class="md-ellipsis">`{=html} Linux - Privilege Escalation

`</span>`{=html}

`</a>`{=html}

</li>
<li class="md-nav__item">

`<a href="../MSSQL%20Server%20-%20Cheatsheet/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} MSSQL Server

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../Metasploit%20-%20Cheatsheet/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Metasploit

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../Methodology%20and%20enumeration/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Bug Hunting Methodology and
Enumeration

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../Network%20Discovery/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Network Discovery

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../Network%20Pivoting%20Techniques/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Network Pivoting Techniques

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../Office%20-%20Attacks/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Office - Attacks

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../Powershell%20-%20Cheatsheet/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Powershell

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../Reverse%20Shell%20Cheatsheet/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Reverse Shell Cheat Sheet

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../Source%20Code%20Management/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Source Code Management & CI/CD
Compromise

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../Vulnerability%20Reports/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Vulnerability Reports

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../Web%20Attack%20Surface/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Subdomains Enumeration

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../Windows%20-%20AMSI%20Bypass/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Windows - AMSI Bypass

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../Windows%20-%20DPAPI/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Windows - DPAPI

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../Windows%20-%20Defenses/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Windows - Defenses

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../Windows%20-%20Download%20and%20Execute/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Windows - Download and execute
methods

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../Windows%20-%20Mimikatz/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Windows - Mimikatz

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../Windows%20-%20Persistence/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Windows - Persistence

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../Windows%20-%20Privilege%20Escalation/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Windows - Privilege Escalation

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../Windows%20-%20Using%20credentials/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Windows - Using credentials

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_39" >
        
          
          <label class="md-nav__link" for="__nav_39" id="__nav_39_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} NoSQL Injection

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_39_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_39">
            <span class="md-nav__icon md-icon"></span>
            NoSQL Injection
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../NoSQL%20Injection/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} NoSQL Injection

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_40" >
        
          
          <label class="md-nav__link" for="__nav_40" id="__nav_40_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} OAuth Misconfiguration

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_40_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_40">
            <span class="md-nav__icon md-icon"></span>
            OAuth Misconfiguration
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../OAuth%20Misconfiguration/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} OAuth Misconfiguration

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_41" >
        
          
          <label class="md-nav__link" for="__nav_41" id="__nav_41_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} ORM Leak

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_41_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_41">
            <span class="md-nav__icon md-icon"></span>
            ORM Leak
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../ORM%20Leak/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} ORM Leak

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_42" >
        
          
          <label class="md-nav__link" for="__nav_42" id="__nav_42_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} Open Redirect

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_42_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_42">
            <span class="md-nav__icon md-icon"></span>
            Open Redirect
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../Open%20Redirect/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Open URL Redirect

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_43" >
        
          
          <label class="md-nav__link" for="__nav_43" id="__nav_43_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} Prompt Injection

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_43_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_43">
            <span class="md-nav__icon md-icon"></span>
            Prompt Injection
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../Prompt%20Injection/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Prompt Injection

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_44" >
        
          
          <label class="md-nav__link" for="__nav_44" id="__nav_44_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} Prototype Pollution

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_44_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_44">
            <span class="md-nav__icon md-icon"></span>
            Prototype Pollution
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../Prototype%20Pollution/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Prototype Pollution

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_45" >
        
          
          <label class="md-nav__link" for="__nav_45" id="__nav_45_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} Race Condition

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_45_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_45">
            <span class="md-nav__icon md-icon"></span>
            Race Condition
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../Race%20Condition/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Race Condition

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_46" >
        
          
          <label class="md-nav__link" for="__nav_46" id="__nav_46_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} Regular Expression

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_46_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_46">
            <span class="md-nav__icon md-icon"></span>
            Regular Expression
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../Regular%20Expression/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Regular Expression

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_47" >
        
          
          <label class="md-nav__link" for="__nav_47" id="__nav_47_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} Request Smuggling

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_47_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_47">
            <span class="md-nav__icon md-icon"></span>
            Request Smuggling
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../Request%20Smuggling/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Request Smuggling

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_48" >
        
          
          <label class="md-nav__link" for="__nav_48" id="__nav_48_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} Reverse Proxy Misconfigurations

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_48_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_48">
            <span class="md-nav__icon md-icon"></span>
            Reverse Proxy Misconfigurations
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../Reverse%20Proxy%20Misconfigurations/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Reverse Proxy Misconfigurations

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_49" >
        
          
          <label class="md-nav__link" for="__nav_49" id="__nav_49_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} SAML Injection

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_49_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_49">
            <span class="md-nav__icon md-icon"></span>
            SAML Injection
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../SAML%20Injection/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} SAML Injection

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_50" >
        
          
          <label class="md-nav__link" for="__nav_50" id="__nav_50_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} SQL Injection

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_50_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_50">
            <span class="md-nav__icon md-icon"></span>
            SQL Injection
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../SQL%20Injection/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} SQL Injection

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../SQL%20Injection/BigQuery%20Injection/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Google BigQuery SQL Injection

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../SQL%20Injection/Cassandra%20Injection/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Cassandra Injection

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../SQL%20Injection/DB2%20Injection/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} DB2 Injection

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../SQL%20Injection/MSSQL%20Injection/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} MSSQL Injection

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../SQL%20Injection/MySQL%20Injection/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} MySQL Injection

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../SQL%20Injection/OracleSQL%20Injection/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Oracle SQL Injection

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../SQL%20Injection/PostgreSQL%20Injection/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} PostgreSQL Injection

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../SQL%20Injection/SQLite%20Injection/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} SQLite Injection

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../SQL%20Injection/SQLmap/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} SQLmap

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_51" >
        
          
          <label class="md-nav__link" for="__nav_51" id="__nav_51_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} Server Side Include Injection

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_51_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_51">
            <span class="md-nav__icon md-icon"></span>
            Server Side Include Injection
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../Server%20Side%20Include%20Injection/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Server Side Include Injection

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_52" >
        
          
          <label class="md-nav__link" for="__nav_52" id="__nav_52_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} Server Side Request Forgery

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_52_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_52">
            <span class="md-nav__icon md-icon"></span>
            Server Side Request Forgery
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../Server%20Side%20Request%20Forgery/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Server-Side Request Forgery

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../Server%20Side%20Request%20Forgery/SSRF-Advanced-Exploitation/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} SSRF Advanced Exploitation

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../Server%20Side%20Request%20Forgery/SSRF-Cloud-Instances/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} SSRF URL for Cloud Instances

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_53" >
        
          
          <label class="md-nav__link" for="__nav_53" id="__nav_53_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} Server Side Template Injection

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_53_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_53">
            <span class="md-nav__icon md-icon"></span>
            Server Side Template Injection
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../Server%20Side%20Template%20Injection/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Server Side Template Injection

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../Server%20Side%20Template%20Injection/ASP/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Server Side Template Injection -
ASP.NET

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../Server%20Side%20Template%20Injection/Java/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Server Side Template Injection -
Java

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../Server%20Side%20Template%20Injection/JavaScript/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Server Side Template Injection -
JavaScript

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../Server%20Side%20Template%20Injection/PHP/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Server Side Template Injection - PHP

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../Server%20Side%20Template%20Injection/Python/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Server Side Template Injection -
Python

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../Server%20Side%20Template%20Injection/Ruby/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Server Side Template Injection -
Ruby

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_54" >
        
          
          <label class="md-nav__link" for="__nav_54" id="__nav_54_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} Tabnabbing

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_54_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_54">
            <span class="md-nav__icon md-icon"></span>
            Tabnabbing
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../Tabnabbing/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Tabnabbing

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_55" >
        
          
          <label class="md-nav__link" for="__nav_55" id="__nav_55_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} Type Juggling

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_55_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_55">
            <span class="md-nav__icon md-icon"></span>
            Type Juggling
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../Type%20Juggling/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Type Juggling

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_56" >
        
          
          <label class="md-nav__link" for="__nav_56" id="__nav_56_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} Upload Insecure Files

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_56_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_56">
            <span class="md-nav__icon md-icon"></span>
            Upload Insecure Files
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../Upload%20Insecure%20Files/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Upload Insecure Files

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item md-nav__item--nested">

`<input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_56_2" >`{=html}

    <label class="md-nav__link" for="__nav_56_2" id="__nav_56_2_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} Configuration Apache .htaccess

`</span>`{=html}

      <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="2" aria-labelledby="__nav_56_2_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_56_2">
            <span class="md-nav__icon md-icon"></span>
            Configuration Apache .htaccess
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../Upload%20Insecure%20Files/Configuration%20Apache%20.htaccess/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} .htaccess

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>




          </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_57" >
        
          
          <label class="md-nav__link" for="__nav_57" id="__nav_57_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} Virtual Hosts

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_57_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_57">
            <span class="md-nav__icon md-icon"></span>
            Virtual Hosts
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../Virtual%20Hosts/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Virtual Host

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_58" >
        
          
          <label class="md-nav__link" for="__nav_58" id="__nav_58_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} Web Cache Deception

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_58_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_58">
            <span class="md-nav__icon md-icon"></span>
            Web Cache Deception
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../Web%20Cache%20Deception/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Web Cache Deception

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_59" >
        
          
          <label class="md-nav__link" for="__nav_59" id="__nav_59_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} Web Sockets

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_59_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_59">
            <span class="md-nav__icon md-icon"></span>
            Web Sockets
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../Web%20Sockets/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Web Sockets

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_60" >
        
          
          <label class="md-nav__link" for="__nav_60" id="__nav_60_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} XPATH Injection

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_60_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_60">
            <span class="md-nav__icon md-icon"></span>
            XPATH Injection
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../XPATH%20Injection/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} XPATH Injection

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_61" >
        
          
          <label class="md-nav__link" for="__nav_61" id="__nav_61_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} XSLT Injection

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_61_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_61">
            <span class="md-nav__icon md-icon"></span>
            XSLT Injection
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../XSLT%20Injection/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} XSLT Injection

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_62" >
        
          
          <label class="md-nav__link" for="__nav_62" id="__nav_62_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} XSS Injection

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_62_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_62">
            <span class="md-nav__icon md-icon"></span>
            XSS Injection
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../XSS%20Injection/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Cross Site Scripting

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../XSS%20Injection/1%20-%20XSS%20Filter%20Bypass/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} XSS Filter Bypass

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../XSS%20Injection/2%20-%20XSS%20Polyglot/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Polyglot XSS

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../XSS%20Injection/3%20-%20XSS%20Common%20WAF%20Bypass/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Common WAF Bypass

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../XSS%20Injection/4%20-%20CSP%20Bypass/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} CSP Bypass

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../XSS%20Injection/5%20-%20XSS%20in%20Angular/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} XSS in Angular and AngularJS

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_63" >
        
          
          <label class="md-nav__link" for="__nav_63" id="__nav_63_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} XXE Injection

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_63_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_63">
            <span class="md-nav__icon md-icon"></span>
            XXE Injection
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../XXE%20Injection/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} XML External Entity

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_64" >
        
          
          <label class="md-nav__link" for="__nav_64" id="__nav_64_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} Zip Slip

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_64_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_64">
            <span class="md-nav__icon md-icon"></span>
            Zip Slip
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../Zip%20Slip/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Zip Slip

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_65" >
        
          
          <label class="md-nav__link" for="__nav_65" id="__nav_65_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} LEARNING AND SOCIALS

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_65_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_65">
            <span class="md-nav__icon md-icon"></span>
             LEARNING AND SOCIALS
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../_LEARNING_AND_SOCIALS/BOOKS/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Books

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../_LEARNING_AND_SOCIALS/TWITTER/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Twitter

`</span>`{=html}

`</a>`{=html}
</li>
<li class="md-nav__item">

`<a href="../../_LEARNING_AND_SOCIALS/YOUTUBE/" class="md-nav__link">`{=html}

`<span class="md-ellipsis">`{=html} Youtube

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>














    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_66" >
        
          
          <label class="md-nav__link" for="__nav_66" id="__nav_66_label" tabindex="0">
            

`<span class="md-ellipsis">`{=html} template vuln

`</span>`{=html}

        <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_66_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_66">
            <span class="md-nav__icon md-icon"></span>
             template vuln
          </label>
          <ul class="md-nav__list" data-md-scrollfix>
            
              
                




    <li class="md-nav__item">
      <a href="../../_template_vuln/" class="md-nav__link">
        

`<span class="md-ellipsis">`{=html} Vulnerability Title

`</span>`{=html}

`</a>`{=html}
</li>

      </ul>
        </nav>
      
    </li>

</ul>
</nav>

                  </div>
                </div>
              </div>
            
            
              
              <div class="md-sidebar md-sidebar--secondary" data-md-component="sidebar" data-md-type="toc" >
                <div class="md-sidebar__scrollwrap">
                  <div class="md-sidebar__inner">
                    

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
</nav>

                  </div>
                </div>
              </div>
            
          
          
            <div class="md-content" data-md-component="content">
              <article class="md-content__inner md-typeset">
                

                  



    <a href="https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology and Resources/Linux - Privilege Escalation.md" title="Edit this page" class="md-content__button md-icon" rel="edit">
      
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M10 20H6V4h7v5h5v3.1l2-2V8l-6-6H6c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h4zm10.2-7c.1 0 .3.1.4.2l1.3 1.3c.2.2.2.6 0 .8l-1 1-2.1-2.1 1-1c.1-.1.2-.2.4-.2m0 3.9L14.1 23H12v-2.1l6.1-6.1z"/></svg>
    </a>





    <a href="https://github.com/swisskyrepo/PayloadsAllTheThings/raw/master/Methodology and Resources/Linux - Privilege Escalation.md" title="View source of this page" class="md-content__button md-icon">
      
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M17 18c.56 0 1 .44 1 1s-.44 1-1 1-1-.44-1-1 .44-1 1-1m0-3c-2.73 0-5.06 1.66-6 4 .94 2.34 3.27 4 6 4s5.06-1.66 6-4c-.94-2.34-3.27-4-6-4m0 6.5a2.5 2.5 0 0 1-2.5-2.5 2.5 2.5 0 0 1 2.5-2.5 2.5 2.5 0 0 1 2.5 2.5 2.5 2.5 0 0 1-2.5 2.5M9.27 20H6V4h7v5h5v4.07c.7.08 1.36.25 2 .49V8l-6-6H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h4.5a8.2 8.2 0 0 1-1.23-2"/></svg>
    </a>

<h1 id="linux-privilege-escalation">
Linux - Privilege Escalation
</h1>
<p>
`<img alt="⚠" class="twemoji" src="https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/26a0.svg" title=":warning:" />`{=html}
Content of this page has been moved to
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/">`{=html}InternalAllTheThings/redteam/persistence/linux-persistence`</a>`{=html}
</p>
<ul>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#tools">`{=html}Tools`</a>`{=html}
</li>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#checklists">`{=html}Checklist`</a>`{=html}
</li>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#looting-for-passwords">`{=html}Looting
for passwords`</a>`{=html}
<ul>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#files-containing-passwords">`{=html}Files
containing passwords`</a>`{=html}
</li>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#old-passwords-in-etcsecurityopasswd">`{=html}Old
passwords in /etc/security/opasswd`</a>`{=html}
</li>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#last-edited-files">`{=html}Last
edited files`</a>`{=html}
</li>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#in-memory-passwords">`{=html}In
memory passwords`</a>`{=html}
</li>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#find-sensitive-files">`{=html}Find
sensitive files`</a>`{=html}
</li>
</ul>
</li>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#ssh-key">`{=html}SSH
Key`</a>`{=html}
<ul>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#sensitive-files">`{=html}Sensitive
files`</a>`{=html}
</li>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#ssh-key-predictable-prng-authorized_keys-process">`{=html}SSH
Key Predictable PRNG (Authorized_Keys) Process`</a>`{=html}
</li>
</ul>
</li>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#scheduled-tasks">`{=html}Scheduled
tasks`</a>`{=html}
<ul>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#cron-jobs">`{=html}Cron
jobs`</a>`{=html}
</li>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#systemd-timers">`{=html}Systemd
timers`</a>`{=html}
</li>
</ul>
</li>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#suid">`{=html}SUID`</a>`{=html}
<ul>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#find-suid-binaries">`{=html}Find
SUID binaries`</a>`{=html}
</li>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#create-a-suid-binary">`{=html}Create
a SUID binary`</a>`{=html}
</li>
</ul>
</li>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#capabilities">`{=html}Capabilities`</a>`{=html}
<ul>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#list-capabilities-of-binaries">`{=html}List
capabilities of binaries`</a>`{=html}
</li>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#edit-capabilities">`{=html}Edit
capabilities`</a>`{=html}
</li>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#interesting-capabilities">`{=html}Interesting
capabilities`</a>`{=html}
</li>
</ul>
</li>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#sudo">`{=html}SUDO`</a>`{=html}
<ul>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#nopasswd">`{=html}NOPASSWD`</a>`{=html}
</li>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#ld_preload-and-nopasswd">`{=html}LD_PRELOAD
and NOPASSWD`</a>`{=html}
</li>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#doas">`{=html}Doas`</a>`{=html}
</li>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#sudo_inject">`{=html}sudo_inject`</a>`{=html}
</li>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#cve-2019-14287">`{=html}CVE-2019-14287`</a>`{=html}
</li>
</ul>
</li>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#gtfobins">`{=html}GTFOBins`</a>`{=html}
</li>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#wildcard">`{=html}Wildcard`</a>`{=html}
</li>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#writable-files">`{=html}Writable
files`</a>`{=html}
<ul>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#writable-etcpasswd">`{=html}Writable
/etc/passwd`</a>`{=html}
</li>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#writable-etcsudoers">`{=html}Writable
/etc/sudoers`</a>`{=html}
</li>
</ul>
</li>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#nfs-root-squashing">`{=html}NFS
Root Squashing`</a>`{=html}
</li>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#shared-library">`{=html}Shared
Library`</a>`{=html}
<ul>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#ldconfig">`{=html}ldconfig`</a>`{=html}
</li>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#rpath">`{=html}RPATH`</a>`{=html}
</li>
</ul>
</li>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#groups">`{=html}Groups`</a>`{=html}
<ul>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#docker">`{=html}Docker`</a>`{=html}
</li>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#lxclxd">`{=html}LXC/LXD`</a>`{=html}
</li>
</ul>
</li>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#hijack-tmux-session">`{=html}Hijack
TMUX session`</a>`{=html}
</li>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#kernel-exploits">`{=html}Kernel
Exploits`</a>`{=html}
<ul>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#cve-2022-0847-dirtypipe">`{=html}CVE-2022-0847
(DirtyPipe)`</a>`{=html}
</li>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#cve-2016-5195-dirtycow">`{=html}CVE-2016-5195
(DirtyCow)`</a>`{=html}
</li>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#cve-2010-3904-rds">`{=html}CVE-2010-3904
(RDS)`</a>`{=html}
</li>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#cve-2010-4258-full-nelson">`{=html}CVE-2010-4258
(Full Nelson)`</a>`{=html}
</li>
<li>
`<a href="https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/#cve-2012-0056-mempodipper">`{=html}CVE-2012-0056
(Mempodipper)`</a>`{=html}
</li>
</ul>
</li>
</ul>
<aside class="md-source-file">

[ [
`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">`{=html}`<path d="M21 13.1c-.1 0-.3.1-.4.2l-1 1 2.1 2.1 1-1c.2-.2.2-.6 0-.8l-1.3-1.3c-.1-.1-.2-.2-.4-.2m-1.9 1.8-6.1 6V23h2.1l6.1-6.1zM12.5 7v5.2l4 2.4-1 1L11 13V7zM11 21.9c-5.1-.5-9-4.8-9-9.9C2 6.5 6.5 2 12 2c5.3 0 9.6 4.1 10 9.3-.3-.1-.6-.2-1-.2s-.7.1-1 .2C19.6 7.2 16.2 4 12 4c-4.4 0-8 3.6-8 8 0 4.1 3.1 7.5 7.1 7.9l-.1.2z"/>`{=html}`</svg>`{=html}
]{.md-icon title="Last update"} [March 24,
2025]{.git-revision-date-localized-plugin
.git-revision-date-localized-plugin-date
title="March 24, 2025 15:00:54 UTC"} ]{.md-source-file__fact}

</aside>

::: social-container
    <b>Share this content</b>
    <div class="a2a_kit a2a_kit_size_32 a2a_default_style">
      <a class="a2a_dd" href="https://www.addtoany.com/share"></a>
      <a class="a2a_button_x"></a>
      <a class="a2a_button_telegram"></a>
      <a class="a2a_button_linkedin"></a>
      <a class="a2a_button_email"></a>
      <a class="a2a_button_microsoft_teams"></a>
    </div>
    <br>
    <script async src="https://static.addtoany.com/menu/page.js"></script>
    <script defer src="https://cloud.umami.is/script.js" data-website-id="82be5164-e1f3-4cb0-bd22-20e02086d3d4"></script>
:::

              </article>
            </div>
          
          

<script>var target=document.getElementById(location.hash.slice(1));target&&target.name&&(target.checked=target.name.startsWith("__tabbed_"))</script>

        </div>
        
          <button type="button" class="md-top md-icon" data-md-component="top" hidden>

`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">`{=html}`<path d="M13 20h-2V8l-5.5 5.5-1.42-1.42L12 4.16l7.92 7.92-1.42 1.42L13 8z"/>`{=html}`</svg>`{=html}
Back to top `</button>`{=html}

      </main>
      
        <footer class="md-footer">

::: {.md-footer-meta .md-typeset}
    <div class="md-footer-meta__inner md-grid">
      <div class="md-copyright">


    Made with
    <a href="https://squidfunk.github.io/mkdocs-material/" target="_blank" rel="noopener">
      Material for MkDocs
    </a>
:::

    </div>
:::::::::::::

</footer>
</div>

::: {.md-dialog data-md-component="dialog"}
      <div class="md-dialog__inner md-typeset"></div>
    </div>



      
      <script id="__config" type="application/json">{"base": "../..", "features": ["content.code.copy", "content.action.edit", "content.action.view", "content.tooltips", "navigation.tracking", "navigation.top", "search.share", "search.suggest"], "search": "../../assets/javascripts/workers/search.d50fe291.min.js", "tags": null, "translations": {"clipboard.copied": "Copied to clipboard", "clipboard.copy": "Copy to clipboard", "search.result.more.one": "1 more on this page", "search.result.more.other": "# more on this page", "search.result.none": "No matching documents", "search.result.one": "1 matching document", "search.result.other": "# matching documents", "search.result.placeholder": "Type to start searching", "search.result.term.missing": "Missing", "select.version": "Select version"}, "version": null}</script>


      <script src="../../assets/javascripts/bundle.50899def.min.js"></script>
      

</body>
</html>
:::
