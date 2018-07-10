# prdcloner
Tool to assist in creating DEV server copies of PRD sites using blogvault export links

## Installation
If the tool has not been installed then clone this repo  
`git clone git@github.com:welenofsky/prdcloner.git`

Then you need to install it with pip3  
`pip3 install ./prdcloner`

## Usage
The flow to use this tool is that you have a site backed up to blogvault and you have an existing repo for the site. So requirements are
- a git repo for this site
- a blogvault download URL

When you have those `cd` to the public_html folder for the site. Then in that folder run the command (Make sure to replace the blogvault link and the github link):  
`prdclone https://blogvault/download/link.zip git@github.com:three29/wordpress-site.com`  
See kick the tires below for more info. 

## Kick the tires
What does it do under the hood? It runs this command  
```bash
git clone <SSH REPO URL> . && wget -O file.zip <BLOGVAUL LINK> && unzip -o file.zip && grep -e 'DB_PASSWORD' -e 'DB_NAME' -e 'DB_USER' wp-config.php | sort | awk '{ print $2 }' | grep -oh "[\'\"].*[\'\"]" | tr '\n' ' ' | tr -d '"' | tr -d "'" | awk '{ system("mysql -u " $3 " --password=" $2 " " $1 " < bvfulldump.sql") }'
```

The steps of that command are as follows
1. Clone repo to current directory
2. Download the blogvault link provided and name it file.zip. The script expects a zip file. See next step.
3. Unzip file.zip in place, overwriting the current directories files if name matches whats in zip. This ensures our repo has all changes from PRD in it.
4. Find/Extract the database credentials from wp-config.php.
5. Use those credentials to import the mysql file `bvfulldump.sql` which is provided by blogvault
