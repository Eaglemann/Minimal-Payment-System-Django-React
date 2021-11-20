import {
  Button,
  Card,
  CardContent,
  CardHeader,
  TextField,
} from "@material-ui/core";
import { useEffect, useState } from "react";
import axios from 'axios';


export const Seller = ({ sellerId }: { sellerId: string }) => {
  const [seller, setSeller] = useState<{
    id: number;
    name: string;
    handle: string;
  } | null>(null);
  const [fetchSellerError, setFetchSellerError] = useState<string | null>(null);
  const [handle, setHandle] = useState("")

  const addNewHandle = async (any: any) => {

    await axios({
      method: 'put',
      url: `http://localhost:8000/api/sellers/${sellerId}/`,
      headers: {
        'Content-type': 'application/json'
      },
      responseType: 'json',
      data: handle
    }).then(response => {
      console.log(response.data);
    })
  }


  useEffect(() => {
    fetch(`/api/sellers/${sellerId}`)
      .then(async (res) => {
        if (!res.ok) throw new Error("Failed to fetch seller");

        const data = await res.json();
        setSeller(data);
      })
      .catch((err) => {
        setFetchSellerError(err.message);
      });
  }, [sellerId]);

  if (fetchSellerError) {
    return <div>{fetchSellerError}</div>;
  }

  if (!seller) {
    return <div>pending</div>;
  }


  return (
    <Card>
      <CardHeader title="Edit seller" subheader="Make changes to a seller" />
      <CardContent>
        <form noValidate autoComplete="off">
          <TextField
            id="sellerId"
            label="Seller ID"
            fullWidth={true}
            style={{ margin: 8 }}
            value={seller.id}
            disabled={true}
          />
          <TextField
            id="sellerName"
            label="Seller Name"
            fullWidth={true}
            style={{ margin: 8 }}
            value={seller.name}
            disabled={true}
          />
          <TextField
            id="sellerHandle"
            label="Seller Handle"
            fullWidth={true}
            style={{ margin: 8 }}
            defaultValue={seller.handle}
            onChange={(e) => setHandle(e.target.value)}
          />
          <Button variant="contained" color="primary" onClick={addNewHandle}>
            Update
          </Button>
        </form>
      </CardContent>
    </Card>
  );
};
