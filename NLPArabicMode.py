import re

# Open the file and read its contents
with open('Txt.txt', 'r',encoding='utf-8') as file:
    file_contents = file.read()


def process_text(text):

    ##### Regex to detect AMFD- followed by numbers ###

    #weight_pattern = r"AMFD-\d+"
    weight_pattern = r"(AMFD|MFI)-\d+"

    # Search for the pattern in the text
    weight_match = re.search(weight_pattern, text)

    #secondary_weight_pattern = r"وزن[هة]\s*ثاني[هة]"
    secondary_weight_pattern = r"وزن[هة]\s*[ثت]اني[هة]"

   # Check if "وزنة ثانية" exists in the text
   #secondary_weight_flag =r"وزن[ه,ة] ثاني[ه,ة]" in text# "وزنة ثانيه" in text
   # secondary_weight_flag = "وزنة ثانيه" in text

    secondary_weight_flag = re.search(secondary_weight_pattern, text)
    # Extract the weight number if found
    numberOfWeight = weight_match.group(0) if weight_match else None

    # Perform some logic based on the detected information
    if numberOfWeight:
        print(f"Detected weight number: {numberOfWeight}")

    if secondary_weight_flag:
        print("Secondary weight detected. Performing specific logic...")

    # You can add additional logic here based on your use case
    return numberOfWeight, bool(secondary_weight_flag)


numberOfWeight, secondary_weight_flag = process_text(file_contents)

print(f'{numberOfWeight} \n W2: {secondary_weight_flag} ')



