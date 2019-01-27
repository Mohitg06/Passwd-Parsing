Passwd Parsing

The idea of this challenge is to parse the UNIX /etc/passwd and /etc/groups files and combine the data into a single json output.

While this utility is a toy, please treat it as a real utility program that could be run in a cron job. That means write production quality code per your standards. Use any of the following languages: Java/Kotlin/Scala, C#/F#, Python, Ruby, Go, JavaScript/TypeScript, or Rust. Please post your solution to a public GitHub (or BitBucket or GitLab) repository or submit a zip archive with the source code. Include instructions for building and running your program.

To aid testing and deployment, the paths to the passwd and groups file should be taken as arguments, defaulting to the standard system path. If the input files are absent or malformed, your script must indicate an error in a manner you feel is appropriate.

The output should be a json object where each key is a username and each value is an object containing the field “uid”, “full_name”, and “groups”. Groups should contain a list of all groups the user is a member of.

An example run of such a program might look like:

>>> passwd-parser

{

"list": {

"uid": "38",

"full_name": "Mailing List Manager",

"groups": []

},

"nobody": {

"uid": "65534",

"full_name": "nobody",

"groups": []

},

"lxd": {

"uid": "106",

"full_name": "",

"groups": []

},

"ubuntu": {

"uid": "1000",

"full_name": "Ubuntu",

"groups": [

"adm",

"cdrom",

"dip",

"docker",

"netdev",

"plugdev",

"floppy",

"dialout",

"audio",

"lxd",

"sudo",

"video"

]

},

"man": {

"uid": "6",

"full_name": "man",

"groups": []

}

}
