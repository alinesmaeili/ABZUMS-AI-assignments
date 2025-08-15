import datetime
from sys import platform
import pandas as pd:

import numpy as np
import random
from datetime import datetime, timedelta
import seaborn as sns
import matplotlib.pyplot as plt

def generate_data(num_events=1000):
    platforms = ['web', 'ios', 'android']
    event_types = ['login', 'play video', 'like', 'comment', 'logout']
    start_date = datetime.now() - timedelta(days=90)
    data = []
    for i in range(num_events):
        timestamp = start_date + timedelta(seconds=random.randint(0, 90*24*3600))
        event_type = random.choice(event_types)
        platform = random.choice(platforms)
        video_id = random.randint(1000, 9999) if event_type in ['play video', 'like', 'comment'] else None
        video_duration = random.randint(30, 600) if event_type == 'play video' else None
        watch_time = random.randint(0, video_duration) if video_duration else None
        data.append({
            'event_id': i,
            'user_id': random.randint(1, 100),
            'timestamp': timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'platform': platform,
            'event_type': event_type,
            'video_id': video_id,
            'video_duration_sec': video_duration,
            'watch_time_sec': watch_time
        })
    return pd.DataFrame(data)

df = generate_data()
df['timestamp'] = pd.to_datetime(df['timestamp'])
engagement_weights = {'comment': 5, 'like': 3, 'play video': 1, 'login': 0, 'logout': 0}
df['engagement_score'] = df['event_type'].map(engagement_weights)
df['date'] = df['timestamp'].dt.date
daily_engagement = df.groupby(['date', 'platform'])['engagement_score'].sum().reset_index()
pivot_df = daily_engagement.pivot(index='date', columns='platform', values='engagement_score')
pivot_df = pivot_df.fillna(0)
plt.figure(figsize=(12, 6))
sns.heatmap(pivot_df, cmap='YlOrRd', linewidths=0.5, linecolor='gray')
plt.title('Daily Engagement Score by Platform')
plt.xlabel('Platform')
plt.ylabel('Date')
plt.tight_layout()
plt.show()
