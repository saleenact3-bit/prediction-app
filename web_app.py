PAGE_2 = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>SIKKIM PRO VIP</title>

<style>

*{
box-sizing:border-box;
}

body{
margin:0;
min-height:100vh;
font-family:Arial,Helvetica,sans-serif;
color:white;

background:
radial-gradient(circle at 50% 30%,#12325f,#07172e 45%,#020817 90%);
}

.page{
max-width:900px;
margin:auto;
padding:50px 25px;
text-align:center;
}

.server{
font-size:42px;
font-weight:900;
letter-spacing:3px;
}

.live{
margin-top:12px;
font-size:24px;
font-weight:bold;
}

.dot{
color:red;
font-size:28px;
animation:blink 1s infinite;
text-shadow:0 0 12px red;
}

@keyframes blink{

0%{opacity:1;}

50%{opacity:.15;}

100%{opacity:1;}

}

.uid{
width:85%;
height:100px;
margin:40px auto;

border:3px solid #00cfff;
border-radius:22px;

display:flex;
align-items:center;
justify-content:center;

font-size:38px;
font-weight:bold;
letter-spacing:10px;

background:#061426;
box-shadow:0 0 20px rgba(0,200,255,.2);
}

.inputs{
display:flex;
flex-direction:column;
gap:25px;
align-items:center;
}

.numberbox{
width:85%;
max-width:700px;
height:90px;

border:3px solid #00cfff;
border-radius:20px;

background:#07172b;

color:white;

font-size:30px;
font-weight:bold;

text-align:center;

outline:none;

letter-spacing:3px;
}

.numberbox::placeholder{
color:#4d7da5;
}

.numberbox:focus{
border-color:#36e7ff;
box-shadow:0 0 20px rgba(0,220,255,.35);
}

.bottom{
margin-top:45px;

display:flex;
justify-content:center;
gap:25px;
}

.btn{
width:180px;
height:65px;

border-radius:18px;

font-size:22px;
font-weight:bold;

display:flex;
align-items:center;
justify-content:center;

text-decoration:none;

cursor:pointer;
}

.back{
border:2px solid #00cfff;
color:#00d9ff;
background:transparent;
}

.connect{
border:none;
background:#18c7e6;
color:#001018;
}

.back:hover{
background:#00cfff;
color:#001018;
}

.connect:hover{
background:#35d9f2;
}

@media(max-width:600px){

.server{
font-size:30px;
}

.uid{
width:95%;
font-size:28px;
height:85px;
}

.numberbox{
width:95%;
height:75px;
font-size:24px;
}

.btn{
width:140px;
height:58px;
font-size:18px;
}

}

</style>
</head>

<body>

<div class="page">

<div class="server">
SERVER CONNECTED
</div>

<div class="live">
LIVE <span class="dot">●</span>
</div>

<div class="uid">
5001
</div>

<div class="inputs">

<input
class="numberbox"
type="number"
placeholder="ENTER NUMBER 1"
inputmode="numeric"
>

<input
class="numberbox"
type="number"
placeholder="ENTER NUMBER 2"
inputmode="numeric"
>

</div>

<div class="bottom">

<a href="/" class="btn back">
BACK
</a>

<a href="/connected" class="btn connect">
CONNECT
</a>

</div>

</div>

</body>
</html>
"""
