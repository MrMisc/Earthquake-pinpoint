
@client.command()
async def study(ctx):
    await ctx.send('``Roger, commencing local examination process..``')
    await ctx.send("Magnitude of requested earthquakes?")
    magnit = await client.wait_for('message', timeout = 30.0, check = lambda message: message.author == ctx.author)
    magn = float(magnit.content)

    await ctx.send("What range of magnitudes do you wish to accept?")
    ROAR = await client.wait_for('message', timeout = 30.0, check = lambda message: message.author == ctx.author)
    suck = float(ROAR.content)

    await ctx.send("Location?")
    loc = await client.wait_for('message', timeout = 30.0, check = lambda message: message.author == ctx.author)
    l0cation = loc.content



    rss_address = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_month.geojson"
    json_data = requests.get(rss_address).json()

    totalcount = json_data['metadata']['count']

    def UtcNow():
        now = datetime.utcnow()
        return now

    Number = []
    magnv = []

    for i in range(totalcount):
        targetloc = json_data['features'][i]['properties']['place']
        magnitude = json_data['features'][i]['properties']['mag']
        if  magn+suck >= magnitude >= magn-suck:
            if l0cation in targetloc:
                location = json_data['features'][i]['properties']['place']
                magn = json_data['features'][i]['properties']['mag']

                azgap = json_data['features'][i]['properties']['gap']
                # The largest azimuthal gap
                longitude = json_data['features'][i]['geometry']['coordinates'][0]
                latitude = json_data['features'][i]['geometry']['coordinates'][1]
                depth = json_data['features'][i]['geometry']['coordinates'][2]
                timeepoch =  json_data['features'][i]['properties']['time']
                timeepochmodified = timeepoch/1000
                normaltime = datetime.fromtimestamp(timeepochmodified, timezone.utc).strftime('%Y-%m-%d %H:%M:%S.%f')
                numbero = i
                await ctx.send(f'```This earthquake happened at {location} \n with a magnitude of {magn} \n at a longtiude of {longitude} degrees, a latitude of {latitude} degrees and depth of {depth}m \n at {normaltime}!\n For your reference, the current time in UTC is {UtcNow()}```')

