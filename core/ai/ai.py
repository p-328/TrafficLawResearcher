from .groq.g import Chatbot
from pandas import DataFrame
import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
import uuid
import dotenv
import os
from django.contrib.staticfiles import finders
dotenv.load_dotenv(finders.find('.env'))

cloudinary.config( 
    cloud_name = os.getenv('CLOUDINARY_CLOUD_NAME'), 
    api_key = os.getenv('CLOUDINARY_API_KEY'), 
    api_secret = os.getenv('CLOUDINARY_API_SECRET'), 
    secure=True
)

_cbot = Chatbot()

def resp(query: str, type: str, data_format: str | None):
    if type == "general":
        return _cbot.respond(query)['answer']
    else:
        list_of_states = """
            Alabama
            Alaska
            Arizona
            Arkansas
            California
            Colorado
            Connecticut
            Delaware
            Florida
            Georgia
            Hawaii
            Idaho
            Illinois
            Indiana
            Iowa
            Kansas
            Kentucky
            Louisiana
            Maine
            Maryland
            Massachusetts
            Michigan
            Minnesota
            Mississippi
            Missouri
            Montana
            Nebraska
            Nevada
            New Hampshire
            New Jersey
            New Mexico
            New York
            North Carolina
            North Dakota
            Ohio
            Oklahoma
            Oregon
            Pennsylvania
            Rhode Island
            South Carolina
            South Dakota
            Tennessee
            Texas
            Utah
            Vermont
            Virginia
            Washington
            West Virginia
            Wisconsin
            Wyoming
        """
        li = [state.strip() for state in list_of_states.splitlines()]
        responses = []
        for state in li:
            built_query = f"Does {state}'s move over law satisfy this criteria? The criteria is {query}. Please answer in this format of data: {data_format}"
            response = _cbot.respond(built_query)['answer']
            responses.append(response)
        df = DataFrame({"State": li, f"Criteria: {query}": responses})
        uuid_unique = uuid.uuid4()
        df.to_csv(path_or_buf=f"{query.replace(" ", "")}{uuid_unique.hex}.csv", encoding="utf-8", index=False)
        upload_res = cloudinary.uploader.upload(f"./{query.replace(" ", "")}{uuid_unique.hex}.csv", public_id=f"{query.replace(" ", "")}{uuid_unique.hex}")
        conclusion_response = _cbot.respond(f"Overall, give a general conclusion on state move over laws based on this criteria. Criteria: {query}. Don't mention specific states.")['answer']
        return (conclusion_response, upload_res["secure_url"])

