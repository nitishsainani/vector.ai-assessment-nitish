import axios from "axios";
import {baseUrl} from "./constants";

class BoardService {
  static async getItems() {
    let response = await axios.get(baseUrl);
    return response.data;
  }
}

export default BoardService;
