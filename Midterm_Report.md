# Project Midterm Report
## Clay Wang, Medhavi Gandhi

### Overview

The music industry impacts our everyday lives. Even our very own president Martha Pollack has noticed this trend of students always listening to music. Being able to find the features that make a song popular would be the key for artists to produce hits. Our project seeks to determine the feasibility of predicting popularity of songs using various features of songs.

### Raw features

Below are some of the features and description of the features used below. This is the raw data that we obtained from our data source, without any transformations.


|  Feature |  Value Type | Description  |
|:---------|:-------------|:-----------|
| duration_ms | int | Duration of song in milliseconds |
| key | int | The overall key of the song, where 0 = C, 1 = C#, etc. |
| mode | int | 0 = Major, 1 = Minor |
| acousticness | float  | Rating from 0 to 1 on how acoustic songs are |
| danceability | float  | Rating from 0 to 1 on how suitable a song is for dancing |
| energy  | float  | Measure from 0 to 1 that represents a measure of intensity  |
| instrumentalness | float | Measure from 0 to 1 that represents the likeliness of containing no vocal content |
| loudness | float | Loudness of song in decibels |
| speechiness | float | Measure from 0 to 1 |
| valence | float | Measure of how happy a song is from 0 to 1 |
| tempo | float | Tempo of track in beats per minute |
| release_year | int | Year that the song was released |
| artist  | string  | The lead artist of the song |
