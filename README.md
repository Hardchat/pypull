<h1>PyPull!   <img src="https://upload.wikimedia.org/wikipedia/en/3/3a/Scapy_logo.png" width="50" height="50"></img><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1024px-Python-logo-notext.svg.png" width="50" height="50"></img><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Ubuntu_logoib.svg/1200px-Ubuntu_logoib.svg.png" height="50" width="50"></img></h1> 

<h3>PyPull is a network listener written in Python3 using Scapy and the ipinfo API module. By listening to incoming UDP traffic you can pull ip addresses and ports.</h3>
<h1>Requirements(Installed by setup.sh) - Tested on Ubuntu LTS 18.04</h1>
<ul><strong><b>
 <li>root/sudo permissions for scapy</li>
 <li>git (Pre-Requisite)</li>
 <li>python3</li>
 <li>python3-pip</li>
 <li>scapy</li>
 <li>ipinfo</li>
 <li>Optional: Free ipinfo account to get your access token  </li>
</ul></b></strong>

<h1>Installation</h1>
<strong>
 Add your ipinfo access token in <a href="pypull.py#L6">Here</a> 
 
 ```
 git clone https://github.com/Hardchat/pypull
 cd pypull
 sh setup.sh
 ```

</strong>

<h1>Usage</h1> 
<b>You can use any file you want containing <u><em>proper</em></u> bpf syntax with this script!</b>

<strong>

```pull filter.txt```

</strong>

<h1>Filtering</h1>

<h3>By default pypull's filter is in "filter.txt" which you can edit to add your desired filters, or use a different file for filtering.</h3>
