# Election_Analysis

## Overview of Election Audit

A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Election of Audit Results

The analysis of the election shows that:

There were 369,711 total votes cast in this congressional election.
The county results for the precinct:
Jefferson cast 10.5% of the vote and 38,855 votes.
Denver cast 82.8% of the vote and 306,055 votes.
Arapahoe cast 6.7% of the vote and 24,801.
Denver county had the largest number of votes.
The candidate results were:
Charles Casper Stockham recieved 23.0% of the vote and 85,213 votes.
Diana DeGette recieved 73.8% of the vote and 272,892 votes.
Raymon Anthony Doane recieved 3.1% of the vote and 11,606 votes.
The winner of the election was Diana DeGette, who recieved 73.8% of the vote and 272,892 vote

Output of code referenced by election_results.txt

![Image of Code Output](https://github.com/clondon0792/Election_Analysis/blob/main/image_2022-06-28_232009547.png)

## Election Audit Summary

I propose that the election commission can use the PyPoll_Challenge.py script, with some modifications, for other elections. Currently, the program is written to analyze the election_results.csv file by iterating through each row and reading the data in the second and third columns, 'County' and 'Candidate', in order to calculate and print the results. There are many different ways in which this code can be altered and used with any election results.

For example, the program can be modified to determine which column to read data from by iterating through the header row. Then files with columns that are arranged in a different order will be analyzed accordingly. The programmer will also no longer have to inspect the data in order to ensure that script is reading the correct columns. Another possiblity is to read data from additional columns in order to calculate and print further results. This is useful for files containing more information, such as the type of ballot or the date that the vote was cast.

This would  result in the utilization of another for loop as was done for county_list and candidate_names. 

for county in count_list:

    county_vote = county_votes.get(county)
    county_vote_percentage = float(county_Vote) / float(total_votes) * 100
    etc.
    
This code would allow us to cycle through numerous metrics which could possibly provide more contextual data. It could, for instance, determine how many ballot id's that end with a 1 or a 0 voted for a specific county or person. This may not be particularly useful, but if given more data the same break down can be done with different metrics.
