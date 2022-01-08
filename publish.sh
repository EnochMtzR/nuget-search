newDir="dist"

if ! [[ -d "$newDir" ]] ; then
    mkdir -p "$newDir"
else
    rm -rf "$newDir"
    mkdir "$newDir"
fi

zip dist/nuget-search-1.0.zip nuget-search.py install_latest.sh install.sh requirements.txt