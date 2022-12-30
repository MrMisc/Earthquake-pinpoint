
@client.command()
async def count(ctx):

    await ctx.send("Past **hour** /**day**/**month** database?")
    choice = await client.wait_for('message', timeout = 30.0, check = lambda message: message.author == ctx.author)

    if "hour" in choice.content:
        rss_address = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
        json_data = requests.get(rss_address).json()

        await ctx.send("What miniumum magnitude?")
        amt = await client.wait_for('message', timeout = 30.0, check = lambda message: message.author == ctx.author)
        amount = ne.evaluate(amt.content)

        totalcount = json_data['metadata']['count']

        Number = []
        for i in range(totalcount):

            magn = json_data['features'][i]['properties']['mag']
            if magn >= amount:
                Number.append(json_data['features'][i]['properties']['place'])   #location

        await ctx.send(f'There were {len(Number)} earthquakes with magnitudes greater than {amount} in the past hour.')

    elif "day" in choice.content:

        rss_address = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
        json_data = requests.get(rss_address).json()

        await ctx.send("What miniumum magnitude?")
        amt = await client.wait_for('message', timeout = 30.0, check = lambda message: message.author == ctx.author)
        amount = ne.evaluate(amt.content)

        totalcount = json_data['metadata']['count']

        Number = []
        for i in range(totalcount):

            magn = json_data['features'][i]['properties']['mag']
            if magn >= amount:
                Number.append(json_data['features'][i]['properties']['place'])   #location

        await ctx.send(f'There were {len(Number)} earthquakes with magnitudes greater than {amount} in the past day.')

    elif "month" in choice.content:

        rss_address = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"
        json_data = requests.get(rss_address).json()

        await ctx.send("What miniumum magnitude?")
        amt = await client.wait_for('message', timeout = 30.0, check = lambda message: message.author == ctx.author)
        amount = float(amt.content)


        totalcount = json_data['metadata']['count']

        Number = []
        for i in range(totalcount):

            # magn = float(json_data['features'][i]['properties']['mag'])
            try:
                magn=float(json_data['features'][i]['properties']['mag'])
            except:
                print(i)
            if magn >= amount:
                Number.append(json_data['features'][i]['properties']['place'])   #location

        await ctx.send(f'There were ~{len(Number)} earthquakes with magnitudes greater than {amount} in the past month.')

@client.command()
async def recent(ctx):
    rss_address = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.geojson"
    json_data = requests.get(rss_address).json()

    location = json_data['features'][0]['properties']['place']
    magn = json_data['features'][0]['properties']['mag']

    azgap = json_data['features'][0]['properties']['gap']
    # The largest azimuthal gap
    longitude = json_data['features'][0]['geometry']['coordinates'][0]
    latitude = json_data['features'][0]['geometry']['coordinates'][1]
    depth = json_data['features'][0]['geometry']['coordinates'][2]
    timeepoch =  json_data['features'][0]['properties']['time']
    timeepochmodified = timeepoch/1000
    normaltime = datetime.fromtimestamp(timeepochmodified, timezone.utc).strftime('%Y-%m-%d %H:%M:%S.%f')



    def UtcNow():
        now = datetime.utcnow()
        return now

    await ctx.send(f'```The most recent earthquake happened at {location} \n with a magnitude of {magn} \n at a longtiude of {longitude} degrees, a latitude of {latitude} degrees and depth of {depth}m \n at {normaltime}!\n For your reference, the current time in UTC is {UtcNow()}```')
    await ctx.send(f'``Take note that the azimuth gap is {azgap}. This value is the largest azimuthal gap between azimuthally adjacent stations (in degrees). In general, the smaller this number, the more reliable is the calculated horizontal position of the earthquake. Earthquake locations in which the azimuthal gap exceeds 180 degrees typically have large location and depth uncertainties.  ``')

@client.command()
async def rec5(ctx):
    rss_address = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.geojson"
    json_data = requests.get(rss_address).json()

    timev = []
    locationv = []
    magnv = []
    azgapv = []
    longitudev = []
    latitudev = []
    depthv = []

    for i in range(5):
        location = json_data['features'][i]['properties']['place']
        locationv.append(location)
        magn = json_data['features'][i]['properties']['mag']
        magnv.append(magn)
        azgap = json_data['features'][i]['properties']['gap']
        azgapv.append(azgap)
        longitude = json_data['features'][i]['geometry']['coordinates'][0]
        latitude = json_data['features'][i]['geometry']['coordinates'][1]
        depth = json_data['features'][i]['geometry']['coordinates'][2]
        longitudev.append(longitude)
        latitudev.append(latitude)
        depthv.append(depth)
        timeepoch =  json_data['features'][i]['properties']['time']
        timeepochmodified = timeepoch/1000
        normaltime = datetime.fromtimestamp(timeepochmodified, timezone.utc).strftime('%Y-%m-%d %H:%M:%S.%f')
        timev.append(normaltime)

    def UtcNow():
        now = datetime.utcnow()
        return now
    for i in range(5):
        await ctx.send(f'```Earthquake happened at {locationv[i]} \n with a magnitude of {magnv[i]} \n at a longtiude of {longitudev[i]} degrees, a latitude of {latitudev[i]} degrees and depth of {depthv[i]}m \n at {timev[i]}!\n ```')
    await ctx.send(f'```For your reference, the current time in UTC is {UtcNow()}```')
