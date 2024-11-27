import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("mytuckshop-1bf49-firebase-adminsdk-0r4r2-07a1f4eb7a.json")
firebase_admin.initialize_app(cred)

db=firestore.client()
