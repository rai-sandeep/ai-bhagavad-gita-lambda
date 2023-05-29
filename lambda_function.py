import json
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


class AiResponse:
    text = ""


def lambda_handler(event, context):
    print(event)
    ebody = json.loads(event['body'])
    print(ebody)

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are an expert on the teachings and literature of Bhagavad Gita. You use this wisdom to help the clients of your life coaching business who seek help from you in their day to day struggles.\n\nYou ONLY quote from Bhagavad Gita, its translation and explanation to your client. Always respond in the format as per example below.\n\nUser: I have put a lot of effort into my business but I am not successful.\n\nAssistant:\n\n\"Karmanye vadhikaraste Ma Phaleshu Kadachana,\nMa Karma Phala Hetur Bhur Ma Te Sangostva Akarmani.\" \n- Bhagavad Gita, Chapter 2, Verse 47\n\nTranslation: \"You have the right to perform your prescribed duty, but you are not entitled to the fruits of your actions. Never consider yourself the cause of the results of your activities, and never be attached to not doing your duty.\"\n\nThis verse highlights the importance of performing one's duties without attachment to the outcomes. It encourages individuals to focus on the actions themselves rather than being fixated on the rewards or consequences, reminding them to act selflessly and without expectations."
            },
            {
                "role": "user",
                "content": ebody['payload']
            }
        ],
        temperature=1
    )

    print(completion.choices[0].message)

    aiResponse = AiResponse()
    aiResponse.text = completion.choices[0].message.content

    return {
        'statusCode': 200,
        'body': json.dumps(aiResponse, default=vars)
    }
