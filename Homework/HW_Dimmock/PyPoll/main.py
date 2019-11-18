# import modules
import csv
import os

#  load file and output file
election_data = os.path.join("Resources", "election_data.csv")
election_analysis = os.path.join("analysis", "election_analysis.txt")

# for counting total Votes
total_votes = 0

# make a list counter for candidates and a dictionary counter for votes 
candidate_options = []
candidate_votes = {}

# for tracking who wins and the winning count
winning_candidate = ""
winning_count = 0

# Read the csv 
#then turn it into a list of dictionaries
with open(election_data) as election_data:
    reader = csv.reader(election_data)

    # header
    header = next(reader)

    # for each on every row...
    for row in reader:

        # run loader animation
        print(". ", end=""),

        # add by 1 to total vote count for every vote
        total_votes = total_votes + 1

        # get the candidates name from every row
        candidate_name = row[2]

        # if statement for if the candidate does not match an already existing candidate
        if candidate_name not in candidate_options:

            # add name to the list of candidates in the running
            candidate_options.append(candidate_name)

            # then begin tracking the ammount of voters that for that candidate
            candidate_votes[candidate_name] = 0

        # then add a vote to that candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# print results and export data to a text file
with open(election_analysis, "w") as txt_file:

    # print final vote count 
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # save final vote count to a text file
    txt_file.write(election_results)

    # loop through counts to see winner
    for candidate in candidate_votes:

        # get vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # get winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # print every candidate's voter count and %
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        # save that to the text file
        txt_file.write(voter_output)

        # print name of winning candidate 
        winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
        print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
