import pandas as pd

data = pd.read_csv('/Users/junsu/Desktop/oss과제 2/2019_kbo_for_kaggle_v2.csv')
#1번 > 각 년도별 , 기준별 순위

print('\n각 년도별 , 기준별 상위 10위 선수 : ')
for year in range(2015, 2019):

    year_data = data[data['year'] == year]
    print('\n'f'{year}년')
    print('순위 [batter_name,H] [batter_name,avg] [batter_name,HR] [batter_name,OBP]')
    H_lst = []
    avg_lst = []
    HR_lst = []
    OBP_lst = []
    lst=[]

    players_H = year_data.nlargest(10, 'H')[['batter_name', 'H']].values.tolist()
    players_avg = year_data.nlargest(10, 'avg')[['batter_name', 'avg']].values.tolist()
    players_HR = year_data.nlargest(10, 'HR')[['batter_name', 'HR']].values.tolist()
    players_OBP = year_data.nlargest(10, 'OBP')[['batter_name', 'OBP']].values.tolist()
    for i in range(10):

        print(f"{i+1} : ", players_H[i] ,players_avg[i] ,players_HR[i] ,players_OBP[i])





#2번 > 포지션에 따른 승리 기여도
data_2018 = data[data['year'] == 2018]
positions = ['포수', '1루수', '2루수', '3루수', '유격수', '좌익수', '중견수', '우익수']
print('2018년 포지션 별 최고 승리 기여 선수 : \n')
for position in positions:
    player = data_2018[data_2018['cp'] == position].nlargest(1, 'war')
    print(f"{position} 최고 승리 기여(WAR) 선수: {player['batter_name'].values[0]}")
#3번 > 상관관계


posi = ['R', 'H', 'HR', 'RBI', 'SB', 'war', 'avg', 'OBP', 'SLG']
cor = data[posi + ['salary']].corr()
salary_cor = cor['salary'].drop('salary')
print('\n연봉과의 상관관계:\n', salary_cor)
high_cor = salary_cor.idxmax()
print(f'가장 높은 상관관계를 가진 통계: {high_cor}')
