import {useEffect, useState} from "react";
import {Grid} from "@mui/material";
import {BackendService} from '../services';
import Loader from "react-loader-spinner";
import "react-loader-spinner/dist/loader/css/react-spinner-loader.css";


function HomePage() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    BackendService.BoardService.getItems().then(setData);
  }, [])

  const getSortedData = () => {
    return (data || []).sort((item1, item2) => item1.position < item2.position ? -1 : 1)
  }

  return(
    <>
      <Grid
        style={{margin: 10}}
        container
        direction="row"
        justifyContent="space-evenly"
        alignItems="center"
      >
        {getSortedData().map(item => {
          return (
            <Grid key={item.id} item xs={4} style={{textAlign: "center"}}>
              <p>{item.title}</p>
              {loading && <Loader
                type="Rings"
                color="#00BFFF"
                height={300}
                width={300}
                timeout={3000}
              />}
              <img onLoad={() => setLoading(false)} src={"https://picsum.photos/300/300"} alt={"board"}/>
            </Grid>
          );
        })}
      </Grid>
    </>
  );
}

export default HomePage;
