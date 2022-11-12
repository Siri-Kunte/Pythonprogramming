#Designing a simple chatbot using if else
print("Hello, I am a chatbot")
print("How may I help you?\n")
print("Hit 1 for Software installation request")
print("Hit 2 for Software update request")
print("Hit 3 for Software uninstall request")
print("Hit 4 for Software repair request")
print("Hit 5 for other request")

#Accepting the user input
userinput = int(input("Enter your choice:"))

#Using if else to process user input
if userinput == 1:
    softwarenedded = input("Please provide the Software name")
elif userinput == 2:
    softwareupdate = input("Please provide the Software name to be updated")
elif userinput == 3:
    softwareuninstall =input("Please provide the Software name to be uninstalled")
elif userinput == 4:
    softwarerepair = input("Please provide the Software name to be repaired")
else:
    otherrequest = input("Please provide the deatails of your request")

print("Thank you for using our service ,Our team will get back to you soon")
