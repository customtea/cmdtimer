# Command Line Timer

## help
```bash
python ./cmdtimer.py --help
usage: cmdtimer.py [-h] [--version] {timer,game,alarm,cron} ...

Commndline Timer

options:
  -h, --help            show this help message and exit
  --version             show program version number and exit

Timer Mode:
  {timer,game,alarm,cron}
                        Mode
    timer               Default Normal Timer
    game                Set Timer from prod mass in game (like Idle Game)
    alarm               [Not Implement] Set Timer from DateTime
    cron                [Not Implement] Set Timer Like 'Cron' Table

python ./cmdtimer.py timer --help
usage: cmdtimer.py timer [-h] [--ring] [--silent] [--repeat] [--sound [File Name]] [--scount [Count]] [--progress] [--gui] [--sec [seccond]] [--min [minutes]] [--hour [hour]]

options:
  -h, --help           show this help message and exit
  --ring               Sounding Chime
  --silent             No Sound
  --repeat             Repeat Timer
  --sound [File Name]  Select Sound File
  --scount [Count]     Sound Count
  --progress           Terminal Progress Bar
  --gui                GUI Progress Bar
  --sec [seccond]      Seccond
  --min [minutes]      Minutes
  --hour [hour]        Hour
  

python ./cmdtimer.py game --help
usage: cmdtimer.py game [-h] [--ring] [--silent] [--repeat] [--sound [File Name]] [--scount [Count]] [--progress] [--gui] [--prod [Production]] [--mass [Mass]]

options:
  -h, --help           show this help message and exit
  --ring               Sounding Chime
  --silent             No Sound
  --repeat             Repeat Timer
  --sound [File Name]  Select Sound File
  --scount [Count]     Sound Count
  --progress           Terminal Progress Bar
  --gui                GUI Progress Bar
  --prod [Production]  Production Rate / sec
  --mass [Mass]        Target Production Mass
```