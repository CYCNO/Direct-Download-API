<div align="center">
<h1 align="center">Direct Download API</h1>
<strong><i>A simple yet powerful API for getting direct download link.</i></strong>
<br>
<br>
<a href="https://www.python.org/">
<img src="https://img.shields.io/badge/MADE%20WITH-PYTHON-red?logoColor=red&logo=Python&style=for-the-badge">
</a>
<a href="https://ddl-api.cycno.repl.co/">
<img src="https://img.shields.io/badge/version-0.1-blue?logo=adguard&style=for-the-badge">
</a>
<a href="https://ddl-api.cycno.repl.co/">
<img src="https://img.shields.io/badge/documentation-green?logo=gitbook&style=for-the-badge">
</a>
</div>

---

## Feautres

 - All Information Of File Is Available
 - No Need To Sign Up Or Usage Of Tokens 
 - Data Is In JSON Format 
 - No Need To Download Anything
 - No Limitation For Usage
 - Switch Between Just Download Link Or ALL Information
 - Very Easy To Use
 
 ## Supported Website

- [AnonFiles](https://anonfiles.com/)
- [Mediafire](https://mediafire.com/)
- [Google Drive](https://drive.google.com/)
- [Myfile](https://myfile.is/)
- [Letsupload](https://letsupload.cc/)
- [Filechan](https://filechan.org/)
- [MegaUpload](https://megaupload.nz/)

## DOCUMENTATION
Documentation is on the home page of api 

```bash
https://ddl-api.cycno.repl.co/
```

## Usage/Examples
For using the api you need to decide the `website` and its file `link`as a parameter
```url
https://ddl-api.cycno.repl.co/{website}?link={link}
```
Lets try with mediafire. you first need a mediafire file link and you will use the link as a parameter
```
https://api.com/mediafire?link=https://www.mediafire.com/file/m1shrkvn91d8508/1.png/view
```
And then you will get the response
```json
{
  "status": "true",
  "data": {
    "file": {
      "url": {
        "directDownload": "https://download1078.mediafire.com/uv3a26g9429g4wyDkH-k2g02xco-tzxv3m1sqxI_CPbwnRQARJ5V0kxS_NF__uZZxqLsXxEGqiphYPMV-WHyLfa5isY3ig/m1shrkvn91d8508/1.png",
        "original": "https://www.mediafire.com/file/m1shrkvn91d8508/1.png/view"
      },
      "metadata": {
        "id": "m1shrkvn91d8508",
        "name": "1",
        "size": {
          "readable": "101.98KB"
        },
        "DateAndTime": {
          "time": "09:09:25",
          "date": "2023-03-23"
        }
      }
    }
  }
}
```

## Some Useful Link
- [Api Wrapper in Python](https://github.com/CYCNO/DirectDownload/)

## Contributors
### <a href="https://github.com/CYCNO"><img src="https://avatars.githubusercontent.com/u/90704569?v=4" alt="CYCNO" width="50" height="50" style="border-radius: 50%;"></a>
