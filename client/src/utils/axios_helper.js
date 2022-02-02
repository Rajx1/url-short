import axios from 'axios'

export const axios_helper = axios.create({ baseURL: "https://catfact.ninja" })