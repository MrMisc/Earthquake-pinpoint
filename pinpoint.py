
@client.command()
async def pinpoint(ctx):
    await ctx.send('``Roger, commencing pinpoint process..``')
    await ctx.send("Magnitude of requested earthquake?")
    magnit = await client.wait_for('message', timeout = 30.0, check = lambda message: message.author == ctx.author)
    magn = float(magnit.content)

    await ctx.send("Location?")
    loc = await client.wait_for('message', timeout = 30.0, check = lambda message: message.author == ctx.author)
    l0cation = loc.content



    rss_address = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_month.geojson"
    json_data = requests.get(rss_address).json()

    totalcount = json_data['metadata']['count']


    Number = []
    magnv = []

    for i in range(totalcount):
        targetloc = json_data['features'][i]['properties']['place']
        magnitude = json_data['features'][i]['properties']['mag']
        if  magn+0.5 >= magnitude >= magn-0.5:
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
                break



    def UtcNow():
        now = datetime.utcnow()
        return now
    print(numbero)
    await ctx.send(f'```This earthquake happened at {location} \n with a magnitude of {magn} \n at a longtiude of {longitude} degrees, a latitude of {latitude} degrees and depth of {depth}m \n at {normaltime}!\n For your reference, the current time in UTC is {UtcNow()}```')
    await ctx.send(f"This was the {numbero}th entry.Was this correct?")
    resp = await client.wait_for('message', timeout = 30.0, check = lambda message: message.author == ctx.author)
    if 'no' in resp.content:
        for j in range(numbero+2,totalcount):
            targetloc = json_data['features'][j]['properties']['place']
            magnitude = json_data['features'][j]['properties']['mag']
            ans = []
            if  magn+0.5 >= magnitude >= magn-0.5:
                if l0cation in targetloc:
                    locationo = json_data['features'][j]['properties']['place']
                    magno = json_data['features'][j]['properties']['mag']

                    azgapo = json_data['features'][j]['properties']['gap']
                    # The largest azimuthal gap
                    longitudeo = json_data['features'][j]['geometry']['coordinates'][0]
                    latitudeo = json_data['features'][j]['geometry']['coordinates'][1]
                    deptho = json_data['features'][j]['geometry']['coordinates'][2]
                    timeepocho =  json_data['features'][j]['properties']['time']
                    timeepochmodifiedo = timeepocho/1000
                    normaltimeo = datetime.fromtimestamp(timeepochmodifiedo, timezone.utc).strftime('%Y-%m-%d %H:%M:%S.%f')
                    numbero = j
                    ans.append(locationo)
                    break


        await ctx.send(f'```This earthquake happened at {locationo} \n with a magnitude of {magno} \n at a longtiude of {longitudeo} degrees, a latitude of {latitudeo} degrees and depth of {deptho}m \n at {normaltimeo}!\n For your reference, the current time in UTC is {UtcNow()}```')
        await ctx.send(f"What about this one? The {numbero}th entry!")
        resp = await client.wait_for('message', timeout = 30.0, check = lambda message: message.author == ctx.author)
        if 'no' in resp.content:
            for j in range(numbero+2,totalcount):
                targetloc = json_data['features'][j]['properties']['place']
                magnitude = json_data['features'][j]['properties']['mag']
                ans = []
                if  magn+0.5 >= magnitude >= magn-0.5:
                    if l0cation in targetloc:
                        locationo = json_data['features'][j]['properties']['place']
                        magno = json_data['features'][j]['properties']['mag']

                        azgapo = json_data['features'][j]['properties']['gap']
                        # The largest azimuthal gap
                        longitudeo = json_data['features'][j]['geometry']['coordinates'][0]
                        latitudeo = json_data['features'][j]['geometry']['coordinates'][1]
                        deptho = json_data['features'][j]['geometry']['coordinates'][2]
                        timeepocho =  json_data['features'][j]['properties']['time']
                        timeepochmodifiedo = timeepocho/1000
                        normaltimeo = datetime.fromtimestamp(timeepochmodifiedo, timezone.utc).strftime('%Y-%m-%d %H:%M:%S.%f')
                        numbero = j
                        ans.append(locationo)
                        break


            await ctx.send(f'```This earthquake happened at {locationo} \n with a magnitude of {magno} \n at a longtiude of {longitudeo} degrees, a latitude of {latitudeo} degrees and depth of {deptho}m \n at {normaltimeo}!\n For your reference, the current time in UTC is {UtcNow()}```')
            await ctx.send(f"I give up sir! HAVE SOME TEA INSTEAD AND READ THIS! The {numbero}th entry!")
