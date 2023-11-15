import pandas as pd
sms = pd.read_csv(filename, encoding='latin-1')
sms.head()

#한글 처리 방법
# sudo apt-get install -y fonts-nanum
# sudo fc-cache -fv
# rm ~/.cache/matplotlib -rf