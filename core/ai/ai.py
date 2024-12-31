from .groq.g import Chatbot
from pandas import DataFrame
import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
import uuid

cloudinary.config( 
    cloud_name = "dkyawvev9", 
    api_key = "995557162195594", 
    api_secret = "OtUsLowvSH6eta5M_Q8fo2F9tVs", 
    secure=True
)

_cbot = Chatbot()

def resp(query: str, type: str, data_format: str | None):
    if type == "general":
        return _cbot.respond(query)
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
            response = _cbot.respond(built_query)
            responses.append(response)
        df = DataFrame({"State": li, f"Criteria: {query}": responses})
        uuid_unique = uuid.uuid4()
        df.to_csv(path_or_buf=f"{query.replace(" ", "")}{uuid_unique.hex}.csv", encoding="utf-8", index=False)
        upload_res = cloudinary.uploader.upload(f"./{query.replace(" ", "")}{uuid_unique.hex}.csv", public_id=f"{query.replace(" ", "")}{uuid_unique.hex}")
        conclusion_response = _cbot.respond(f"Overall, give a general conclusion on state move over laws based on this criteria. Criteria: {query}. Don't mention specific states.")
        return (conclusion_response, upload_res["secure_url"])

