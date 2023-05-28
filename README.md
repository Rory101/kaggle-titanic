# kaggle-titanic
Code for exploring the Kaggle ML Titanic competition. 


## Setup the Virtual Enviroment
>`. setup_env.sh`
 
The perion (.) is important.

## Setup Kaggle API key
To use the Kaggle API, sign up for a Kaggle account at https://www.kaggle.com. Then go to the 'Account' tab of your user profile (`https://www.kaggle.com/<username>/account`) and select 'Create API Token'. This will trigger the download of `kaggle.json`, a file containing your API credentials. Place this file in the location `~/.kaggle/kaggle.json`.

## Download the data
>`kaggle competitions download -c titanic`

## Submission File Format

You should submit a csv file with exactly 418 entries plus a header row. Your submission will show an error if you have extra columns (beyond `PassengerId` and `Survived`) or rows.

The file should have exactly 2 columns:
- `PassengerId` (sorted in any order)
- `Survived` (contains your binary predictions: 1 for survived, 0 for deceased)

## Making a submission
Make sure the `submission.csv` is in the format explained above.  
>`kaggle competitions submit -c titanic -f submission.csv -m "Message"`

