import predict1

ride = {
    "PULocationID": 10,
    "DOLocationID": 50,
    "trip_distance": 40
}

features = predict1.prepare_features(ride)
pred = predict1.predict(features)
print(pred)