<h1>PyPull   <img src="https://upload.wikimedia.org/wikipedia/en/3/3a/Scapy_logo.png" width="50" height="50"></img><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1024px-Python-logo-notext.svg.png" width="50" height="50"></img><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Ubuntu_logoib.svg/1200px-Ubuntu_logoib.svg.png" height="50" width="50"></img></h1> 

<h3>PyPull is a network listener written in Python3 using Scapy and the ipinfo.io API module. By listening to incoming TCP or UDP traffic you're able to see ip addresses and ports with PyPull and automatically look them up using the ipinfo module.</h3>
<h1>Requirements</h1>
<ul><strong><b>
 <li>root/sudo permissions for scapy</li>
 <li>git (Pre-Requisite)</li>
 <li>Optional: Free <a href="https://ipinfo.io/signup">ipinfo.io</a> account to get your API access token  </li>
</ul></b></strong>

<h1>Installation</h1>
<strong>
 Add your ipinfo access token in <a href="pypull.py#L10">Here</a> 
 
 ```
 git clone https://github.com/Hardchat/pypull;
 cd pypull;
 sh setup.sh;
 source ~/.bashrc

 ```

</strong>

<h1>Usage</h1> 
<b>You can use any file you want containing <em>proper</em> bpf syntax with this script!</b>

<strong>

```
pull filter.txt 
``` 
<b>Alternatively</b> 
```
python3 pypull.py filter.txt
```
</strong>

<h1>Filtering</h1>

<h3>By default pypull's filter is in <code>pypull/filters</code> which you can edit to add your desired filter expressions, or use a different file for filtering.</h3>
