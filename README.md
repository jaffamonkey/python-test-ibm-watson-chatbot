
## Coverage

* Get idalogs for workspace
* Get dialogs for workspace, based on word count
* Show all intents for workspace
* Change message string depending on value assigned to `changeType`
* Full json reports for each intent, with response data
* Summary report of correct matching intents
* Log files for request or Watson API exception errors

`input` folder contains the imported messages files
`report` folder holds the results file with all response data
`logs` folder hold all data related to errors

### Pre-requisistes
```bash
brew update
brew install python3
pip3 install -r requirements.txt
cp config.example.conf config.conf
```
_Complete the config.conf file_

### Before running a script, assign workspace id to the environment variable `SPACE_ID`
```bash
export SPACE_ID=46249c74-af5f-4c0c-9ffc-7058935d4250
```

To get current workspace ids:

```bash
curl -u "workspace-user-id":"workspace-password" "workspace-url"```
```

### To run

```bash
python3 sendallmessages.py
```

### Delete empty log files

```bash
find ./logs/ -type f -size 0 -exec rm -f {} \;
```

### Tidy json response files

From the `report` directory:

```bash
find ./ -exec sed -i '' '1s/^{/[&/' {} \;
find ./ -exec sed -i '' '$ s/.$/]/' {} \;
```

### Run analysis on json responses for different scenarios (compared to baseline)

```bash
python3 jsoncompare.py file1.json file2.json > output.txt
```

### Extract all 1, 2, and 3 word examples and stores in files.

```
python3 extractwordsmatchingcount.py
```