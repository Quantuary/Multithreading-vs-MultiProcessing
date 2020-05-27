        <!DOCTYPE html>
        <html>
        <head>
        <meta charset="utf-8">
        <style type="text/css">
        .markdown-body{
font-family: sans-serif;
font-size:15px;
line-height:1.7;
overflow:hidden;
word-wrap:break-word
}

.markdown-body>*:first-child{
margin-top:0 !important
}

.markdown-body>*:last-child{
margin-bottom:0 !important
}

.markdown-body a.absent{
color:#c00
}

.markdown-body a.anchor{
display:block;
padding-right:6px;
padding-left:30px;
margin-left:-30px;
cursor:pointer;
position:absolute;
top:0;
left:0;
bottom:0
}

.markdown-body a.anchor:focus{
outline:none
}

.markdown-body tt, .markdown-body code, .markdown-body pre {
font-family: Consolas, "Liberation Mono", Courier, monospace;
font-size: 12px;
}
            
.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6{
margin:1em 0 15px;
padding:0;
font-weight:bold;
line-height:1.7;
cursor:text;
position:relative
}

.markdown-body h1 .octicon-link,.markdown-body h2 .octicon-link,.markdown-body h3 .octicon-link,.markdown-body h4 .octicon-link,.markdown-body h5 .octicon-link,.markdown-body h6 .octicon-link{
display:none;
color:#000
}

.markdown-body h1:hover a.anchor,.markdown-body h2:hover a.anchor,.markdown-body h3:hover a.anchor,.markdown-body h4:hover a.anchor,.markdown-body h5:hover a.anchor,.markdown-body h6:hover a.anchor{
text-decoration:none;
line-height:1;
padding-left:8px;
margin-left:-30px;
top:15%
}

.markdown-body h1:hover a.anchor .octicon-link,.markdown-body h2:hover a.anchor .octicon-link,.markdown-body h3:hover a.anchor .octicon-link,.markdown-body h4:hover a.anchor .octicon-link,.markdown-body h5:hover a.anchor .octicon-link,.markdown-body h6:hover a.anchor .octicon-link{
display:inline-block
}

.markdown-body h1 tt,.markdown-body h1 code,.markdown-body h2 tt,.markdown-body h2 code,.markdown-body h3 tt,.markdown-body h3 code,.markdown-body h4 tt,.markdown-body h4 code,.markdown-body h5 tt,.markdown-body h5 code,.markdown-body h6 tt,.markdown-body h6 code{
font-size:inherit
}

.markdown-body h1{
font-size:2.5em;
border-bottom:1px solid #ddd
}

.markdown-body h2{
font-size:2em;
border-bottom:1px solid #eee
}

.markdown-body h3{
font-size:1.5em
}

.markdown-body h4{
font-size:1.2em
}

.markdown-body h5{
font-size:1em
}

.markdown-body h6{
color:#777;
font-size:1em
}

.markdown-body p,.markdown-body blockquote,.markdown-body ul,.markdown-body ol,.markdown-body dl,.markdown-body table,.markdown-body pre{
margin:15px 0
}

.markdown-body hr {
background: rgba(216, 216, 216, 1);
border: 0 none;
color: #ccc;
height: 2px;
padding: 0;
margin: 15px 0;
}

.markdown-body ul,.markdown-body ol{
padding-left:30px
}

.markdown-body ul.no-list,.markdown-body ul.task-list,.markdown-body ol.no-list,.markdown-body ol.task-list{
list-style-type:none;
padding:0
}

.markdown-body ul ul,.markdown-body ul ol,.markdown-body ol ol,.markdown-body ol ul{
margin-top:0;
margin-bottom:0
}

.markdown-body dl{
padding:0
}

.markdown-body dl dt{
font-size:14px;
font-weight:bold;
font-style:italic;
padding:0;
margin-top:15px
}

.markdown-body dl dd{
margin-bottom:15px;
padding:0 15px
}

.markdown-body blockquote{
border-left:4px solid #DDD;
padding:0 15px;
color:#777
}

.markdown-body blockquote>:first-child{
margin-top:0px
}

.markdown-body blockquote>:last-child{
margin-bottom:0px
}

.markdown-body table{
/* width:100%; */
border-collapse: collapse;
border-spacing: 0;
overflow:auto;
display:block
}

.markdown-body table th{
font-weight:bold
}

.markdown-body table th,.markdown-body table td{
border:1px solid #ddd;
padding:6px 13px
}

.markdown-body table tr{
border-top:1px solid #ccc;
background-color:#fff
}

.markdown-body table tr:nth-child(2n){
background-color:#f8f8f8
}

.markdown-body img{
max-width:100%;
-moz-box-sizing:border-box;
box-sizing:border-box
}

.markdown-body span.frame{
display:block;
overflow:hidden
}

.markdown-body span.frame>span{
border:1px solid #ddd;
display:block;
float:left;
overflow:hidden;
margin:13px 0 0;
padding:7px;
width:auto
}

.markdown-body span.frame span img{
display:block;
float:left
}

.markdown-body span.frame span span{
clear:both;
color:#333;
display:block;
padding:5px 0 0
}

.markdown-body span.align-center{
display:block;
overflow:hidden;
clear:both
}

.markdown-body span.align-center>span{
display:block;
overflow:hidden;
margin:13px auto 0;
text-align:center
}

.markdown-body span.align-center span img{
margin:0 auto;
text-align:center
}

.markdown-body span.align-right{
display:block;
overflow:hidden;
clear:both
}

.markdown-body span.align-right>span{
display:block;
overflow:hidden;
margin:13px 0 0;
text-align:right
}

.markdown-body span.align-right span img{
margin:0;
text-align:right
}

.markdown-body span.float-left{
display:block;
margin-right:13px;
overflow:hidden;
float:left
}

.markdown-body span.float-left span{
margin:13px 0 0
}

.markdown-body span.float-right{
display:block;
margin-left:13px;
overflow:hidden;
float:right
}

.markdown-body span.float-right>span{
display:block;
overflow:hidden;
margin:13px auto 0;
text-align:right
}

.markdown-body code,.markdown-body tt{
margin:0;
border:1px solid #ddd;
background-color:#f8f8f8;
border-radius:3px;
max-width:100%;
display:inline-block;
overflow:auto;
vertical-align:middle;
line-height:1.3;
padding:0
}

.markdown-body code:before,.markdown-body code:after,.markdown-body tt:before,.markdown-body tt:after{
content:"\00a0"
}

.markdown-body code{
white-space:nowrap
}

.markdown-body pre>code{
margin:0;
padding:0;
white-space:pre;
border:none;
background:transparent
}

.markdown-body .highlight pre,.markdown-body pre{
background-color:#f8f8f8;
border:1px solid #ddd;
font-size:13px;
line-height:19px;
overflow:auto;
padding:6px 10px;
border-radius:3px
}

.markdown-body pre{
word-wrap:normal
}

.markdown-body pre code,.markdown-body pre tt{
margin:0;
padding:0;
background-color:transparent;
border:none;
word-wrap:normal;
max-width:initial;
display:inline;
overflow:initial;
line-height:inherit
}

.markdown-body pre code:before,.markdown-body pre code:after,.markdown-body pre tt:before,.markdown-body pre tt:after{
content:normal
}

pre .hll { background-color: #ffffcc }
pre .c { color: #999988; font-style: italic } /* Comment */
pre .err { color: #a61717; background-color: #e3d2d2 } /* Error */
pre .k { color: #000000; font-weight: bold } /* Keyword */
pre .o { color: #000000; font-weight: bold } /* Operator */
pre .cm { color: #999988; font-style: italic } /* Comment.Multiline */
pre .cp { color: #999999; font-weight: bold; font-style: italic } /* Comment.Preproc */
pre .c1 { color: #999988; font-style: italic } /* Comment.Single */
pre .cs { color: #999999; font-weight: bold; font-style: italic } /* Comment.Special */
pre .gd { color: #000000; background-color: #ffdddd } /* Generic.Deleted */
pre .ge { color: #000000; font-style: italic } /* Generic.Emph */
pre .gr { color: #aa0000 } /* Generic.Error */
pre .gh { color: #999999 } /* Generic.Heading */
pre .gi { color: #000000; background-color: #ddffdd } /* Generic.Inserted */
pre .go { color: #888888 } /* Generic.Output */
pre .gp { color: #555555 } /* Generic.Prompt */
pre .gs { font-weight: bold } /* Generic.Strong */
pre .gu { color: #aaaaaa } /* Generic.Subheading */
pre .gt { color: #aa0000 } /* Generic.Traceback */
pre .kc { color: #000000; font-weight: bold } /* Keyword.Constant */
pre .kd { color: #000000; font-weight: bold } /* Keyword.Declaration */
pre .kn { color: #000000; font-weight: bold } /* Keyword.Namespace */
pre .kp { color: #000000; font-weight: bold } /* Keyword.Pseudo */
pre .kr { color: #000000; font-weight: bold } /* Keyword.Reserved */
pre .kt { color: #445588; font-weight: bold } /* Keyword.Type */
pre .m { color: #009999 } /* Literal.Number */
pre .s { color: #d01040 } /* Literal.String */
pre .na { color: #008080 } /* Name.Attribute */
pre .nb { color: #0086B3 } /* Name.Builtin */
pre .nc { color: #445588; font-weight: bold } /* Name.Class */
pre .no { color: #008080 } /* Name.Constant */
pre .nd { color: #3c5d5d; font-weight: bold } /* Name.Decorator */
pre .ni { color: #800080 } /* Name.Entity */
pre .ne { color: #990000; font-weight: bold } /* Name.Exception */
pre .nf { color: #990000; font-weight: bold } /* Name.Function */
pre .nl { color: #990000; font-weight: bold } /* Name.Label */
pre .nn { color: #555555 } /* Name.Namespace */
pre .nt { color: #000080 } /* Name.Tag */
pre .nv { color: #008080 } /* Name.Variable */
pre .ow { color: #000000; font-weight: bold } /* Operator.Word */
pre .w { color: #bbbbbb } /* Text.Whitespace */
pre .mf { color: #009999 } /* Literal.Number.Float */
pre .mh { color: #009999 } /* Literal.Number.Hex */
pre .mi { color: #009999 } /* Literal.Number.Integer */
pre .mo { color: #009999 } /* Literal.Number.Oct */
pre .sb { color: #d01040 } /* Literal.String.Backtick */
pre .sc { color: #d01040 } /* Literal.String.Char */
pre .sd { color: #d01040 } /* Literal.String.Doc */
pre .s2 { color: #d01040 } /* Literal.String.Double */
pre .se { color: #d01040 } /* Literal.String.Escape */
pre .sh { color: #d01040 } /* Literal.String.Heredoc */
pre .si { color: #d01040 } /* Literal.String.Interpol */
pre .sx { color: #d01040 } /* Literal.String.Other */
pre .sr { color: #009926 } /* Literal.String.Regex */
pre .s1 { color: #d01040 } /* Literal.String.Single */
pre .ss { color: #990073 } /* Literal.String.Symbol */
pre .bp { color: #999999 } /* Name.Builtin.Pseudo */
pre .vc { color: #008080 } /* Name.Variable.Class */
pre .vg { color: #008080 } /* Name.Variable.Global */
pre .vi { color: #008080 } /* Name.Variable.Instance */
pre .il { color: #009999 } /* Literal.Number.Integer.Long */


        </style>
        </head>
        <body>
        <div class="markdown-body">
        <h1><a href="https://github.com/Quantuary/Multithreading-vs-MultiProcessing/wiki">WIKI page</a></h1>
        </div>
        </body>
        </html>
        