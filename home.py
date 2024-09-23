import streamlit as st
from streamlit_extras.row import row
from streamlit_extras.grid import grid
from streamlit_extras.tags import tagger_component
import streamlit.components.v1 as components

import constants
import pandas as pd

from services.storage_service import StorageService
from services.metadata_service import MetadataService

import utils

import ui_constants

st.set_page_config(
    page_title="Medical Report Explorer",
    page_icon="🏥",
    layout="wide",    
)

metadata_service = metadata_service = MetadataService()

if ui_constants.SERVICE_STORAGE not in st.session_state:
    with st.spinner('Getting your experience ready...'):
        # Services initialization
        st.session_state[ui_constants.SERVICE_STORAGE] = StorageService([constants.INPUT_BUCKET], constants.SERVICE_ACCOUNT_KEY_FILE)


# Page definition
st.header("Medical Report Explorer")


def build_audio_card(item, index: int):

                
    file_gcs_uri = f"gs://{constants.INPUT_BUCKET}/{item['file_name']}"

    url = utils.get_public_gcs_url(file_gcs_uri)
    cols = st.columns([3,1])
    cols[0].subheader(f"{index+1} : {item['name']}")
    cols[1].link_button("Full Report", url=url, type='secondary')
    st.divider()
    

    st.subheader("Overview")
    # st.divider()

    cols = st.columns(2)

    cols[0].write(f"*Test Type*: {item['metadata']['TestInfo']['Type']}")
    cols[0].write(f"*Report Date*: {item['metadata']['TestInfo']['ReportDate']}")
    cols[1].write(f"*Indications*: {item['metadata']['TestInfo']['Indications']}")
    
    st.write("*Summary*:")
    st.write(f"{item['metadata']['Summary']}")
    st.subheader("Patient ")
    
    st.write(f"*Age*: {item['metadata']['PatientInfo']['Age']}")
    st.write(f"*Gender*: {item['metadata']['PatientInfo']['Sex']}")
    st.write(f"*History*: {item['metadata']['PatientInfo']['RelevantMedicalHistory']}")
    
    st.subheader("Details")
    with st.expander(label = 'Findings', expanded=False):
        st.table(item['metadata']['Findings'])
    with st.expander(label = 'Measurements', expanded=False):
        st.table(item['metadata']['Measurements'])
    


items = metadata_service.list_all_documents()
# st.header(f"Number of Reports : {len(items)}")
st.metric(label="Number of Reports", value=len(items))


content_grid = grid(1, vertical_align="center")
for index, item in enumerate(items):
    if 'metadata' in item:
        with content_grid.container(border=True):
            build_audio_card(item, index)
st.toast('All reports loaded', icon='👍')
