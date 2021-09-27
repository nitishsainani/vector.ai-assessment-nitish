import {useEffect, useState} from "react";
import {Grid} from "@mui/material";
import {BackendService} from '../services';

function HomePage() {
  const [data, setData] = useState([]);

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
              <img src={"https://picsum.photos/300/300"} alt={"image"}/>
            </Grid>
          );
        })}
      </Grid>
    </>
  );
}

export default HomePage;
