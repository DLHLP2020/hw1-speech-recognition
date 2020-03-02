# HW1 ― End-to-end Speech Recognition
In this assignment, you are given a dataset of single speaker audio files. Your task is to perform speech recognition on the dataset.

![](https://i.imgur.com/89NtMwS.png)

For more details, please click [this link](https://docs.google.com/presentation/d/1C2a1_V91EHjy3sgxy3rKWqU6hCIOOsbMWuOhYCZW5jQ) to view the slides of HW1.

### Start
Please create your own private Github repo to host your files. The repo name should be `hw1-speech-recognition`. And you repo link will be `https://github.com/<YOUR_GITHUB_ID>/hw1-speech-recognition`. After that, your **MUST** register `<YOUR_GITHUB_ID>` with [this form](https://forms.gle/G7LohptsqnxFkpWc9), and add [TA's github account](#) to the repo collaborator, or we cannot receive your submission.

### Dataset
In the starter code of this repository, we have provided a shell script for downloading and extracting the dataset for this assignment. For Linux users, simply use the following command.

    bash ./get_dataset.sh
The shell script will automatically download the dataset and store the data in a folder called `data/DLHLP/`. Note that this command by default only works on Linux. If you are using other operating systems, you should download the dataset from [this link](https://docs.google.com/uc?export=download&id=1daFU8tPPUyhN7Fc6JUTohEfHXIn6ZDgq) and unzip the compressed file manually.

> ⚠️  ***Warning*** ⚠️  
> You should keep a copy of the dataset only in your local machine. **DO NOT** upload the dataset to this remote repository. If you extract the dataset manually, be sure to put them in a folder called `data/` under the root directory of your local repository so that it will be included in the default `.gitignore` file.

### Submission Format

<p><strong>All student should submit your answer in CSV format with <code>,</code> as delimiter</strong>. Submission files should contain two columns: <code>id</code> and <code>answer</code>. <code>id</code> should be a six-digits number (e.g. <code>009001</code> according to <code>009001.wav</code> audio file. The answer to the wav file should be put in <code>answer</code> column. There should <strong>NOT</strong> be any space between the <code>answer</code> and delimiter. Sorting according to <code>id</code> is not necessary.

```
id,answer
009001,ㄩˇ ㄧㄣ ㄅㄧㄢˋ ㄕˋ
009002,ㄩˇ ㄧㄣ ㄅㄧㄢˋ ㄕˋ
...,...
009999,ㄩˇ ㄧㄣ ㄅㄧㄢˋ ㄕˋ
010000,ㄩˇ ㄧㄣ ㄅㄧㄢˋ ㄕˋ
```

If you use the sample code ([End-to-end-ASR-Pytorch](https://github.com/Alexander-H-Liu/End-to-end-ASR-Pytorch)), you can produce the result by: 
```
python3 main.py --config <config file> --test --njobs 8
```
After that, use this simple script to format:

```
python3 format.py <result csv file> <output file name>
```


### Evaluation on dev set
To evaluate your model on dev set, you can run the provided evaluation script provided in the starter code by using the following command.

#### Mean Levenshtein Distance
```
python3 eval_lev.py ans.dev.csv <predict_csv_file>
```

#### Word Error Rate (and Char Error Rate)
```
python3 eval_wer.py ans.dev.csv <predict_csv_file>
```

# Submission Rules
### Kaggle Deadline
2020/03/22 (Sun.) 23:59
### All files submission Deadline
2020/03/25(Wed) before class

### Submission Format
Aside from your own Python scripts and model files, you should make sure that your submission includes *at least* the following files in the root directory of this repository:
 1.   `report.pdf`  
The report of your homework assignment. Refer to the "*Report Questions*" section in the slides for what you should include in the report.
 2.   `reproduce.sh`  
The shell script file for running your ASR model. The produced answer should be the same as the best submitted file on kaggle. If the score is not matched, you would lost the 5 points on kaggle.

We will run your code in the following manner:

    bash ./reproduce.sh $1 $2
where `$1` is the audio dataset directory (e.g. `data/DLHLP`), and `$2` is name of the output prediction csv file (e.g. `ans.csv` ).

### Packages
In [`pip-freeze.txt`](https://github.com/DLHLP2020/hw1-speech-recognition/pip-freeze.txt) is a list of packages you are allowed to import in this assignment.

If you only use the machine in 計中, all packages are installed, you don't need to do any thing.

Note that using packages with different versions will very likely lead to compatibility issues when we reproduce your results. If you use your own computer, make sure that you install the correct version as listed in [`pip-freeze.txt`](https://github.com/DLHLP2020/hw1-speech-recognition/pip-freeze.txt). E-mail or ask the TAs first if you want to import other packages.

### Remarks
- If your model is larger than GitHub’s maximum capacity (100MB), you can upload your model to another cloud service (e.g. Dropbox). However, your shell script files should be able to download the model automatically. For a tutorial on how to do this using Dropbox, please click [this link](https://docs.google.com/presentation/d/1SsIeIij9ZOEN_TGdbAS1oWcI6bT1uSTI6b5__u2wdDc/edit?usp=sharing).

# Q&A
If you have any problems related to HW1, you may
- Use TA hours (please check [course website](http://speech.ee.ntu.edu.tw/~tlkagk/courses_DLHLP20.html) for time/location)
- Contact TAs by e-mail ([dlhlp.ta@gmail.com](mailto:dlhlp.ta@gmail.com))
- Post your question in the comment section of [this post](https://www.facebook.com/groups/789568188219010)
