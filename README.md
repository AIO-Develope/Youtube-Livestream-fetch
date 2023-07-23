
<h1 align="center">
    Youtube Livestream fetch
    <br>
    <div align="center">
    <img src="https://img.shields.io/badge/Python-3.10.4-blue" align="center"/>
    <img src="https://img.shields.io/badge/Developing-only on request-brightgreen" align="center"/>
    <img src="https://img.shields.io/badge/Version-1.0-green" align="center"/>
    </div>
</h1>

This small script fetches your current YouTube livestream URL from a YouTube channel and can be placed in a JSON file, as demonstrated in this project.

# Installation
```
Requests==2.31.0
```
To install the requirements run:
```
pip install -r requirements.txt
```

Now rename ```example.config.json``` to config.json and change the informations to youre desire.

If you don't know how to get your Google API key, there are multiple tutorials available on the internet.

```
{
  "channel_id": "youre_channel_id",
  "api_key": "youre_google_api_key",
  "json_file_path": "./links.json"
}
```
# File structure
```
├ example.config.json   // the config file you need
├ links.json            // here is going to be youre livestream link
├ main.py               // the script
└ requirements.txt      // the requirements for this project
```
# Run it
Now you can run it like this:
```
python main.py
```
# Important
This script is specifically designed for another project, and it is quite specific in its functionality. If you need it to be used differently or adapted for another purpose, you will have to make the necessary changes by yourself.
This project is just a randome upload i will not focus on it! but if someone ask for an improvement i will hear it.
