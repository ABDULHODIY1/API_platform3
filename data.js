// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBXszn7U6XW6d2TGRSbyzEe86WHBmr8KRY",
  authDomain: "dataset-75427.firebaseapp.com",
  projectId: "dataset-75427",
  storageBucket: "dataset-75427.appspot.com",
  messagingSenderId: "704709443789",
  appId: "1:704709443789:web:746dfc4f7c6ffd1e656984",
  measurementId: "G-KHC9HSE5TB"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);