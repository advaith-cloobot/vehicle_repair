// httpClient.js
import axios from 'axios';




const PROD_BACK = 'http://192.168.1.10:5000'  

const httpClient = axios.create({
  baseURL: PROD_BACK  
});

// const httpClient = "fkjewhf";



export default httpClient;