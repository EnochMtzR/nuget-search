# nuget-search

**_nuget-search_** is a tiny CLI tool written in Python 3 to search the _Nuget Repository_

## nuget-search VS dotnet-search

You may think _"Yet another nuget search repository"_ or _"Why do I need another tool to search the nuget repository?"_ or perhaps _"What's the difference with dotnet-search?"_

Here are the key points that drove me to create this simple, yet useful tool (at least it is useful for me):

- dotnet-search does not work with .net v.5>= nor with .net core
- I needed a simple way from CLI to search packages instead of going directly to [nuget.org](www.nuget.org) and search for my package.
- Perhaps not the best reason but a reason none the less. I wanted to practice _"Web Scraping"_ with Python

## Installation

Download the [latest release archive](/releases/latest)

```bash
unzip nuget-search-1.0.zip -d nuget-search
cd nuget-search
chmod +x install*
```

If you want to install the bleeding edge unstable release execute `./install_latest.sh`

If you want to install the downloaded release just execute `./install.sh`

## Usage

`nuget-search <query-string>`

this will output something like the following:

```output
Title                                                 Version          Authors                   Downloads
----------------------------------------------------  ---------------  ------------------------  -----------
IdentityServer4                                       4.1.2            ['identity']              26,308,412
IdentityServer4.AccessTokenValidation                 3.0.1            ['identity']              28,085,947
IdentityServer4.Storage                               4.1.2            ['identity']              21,655,901
IdentityServer4.AspNetIdentity                        4.1.2            ['identity']              12,600,611
IdentityModel                                         6.0.0            ['identity']              107,568,390
...
```

which will be followed by a prompt `:` symbolizing now you can input commands the following commands are valid:

- `q` - quits the cli
- `n` or `enter` will output the next page of packages
- `query-string` will change the current query to the one provided.
