

@client.command()
async def sieve(ctx, arg1, arg2):
    await ctx.send("Past **hour** or Past **day** database?")
    choice = await client.wait_for('message', timeout = 30.0, check = lambda message: message.author == ctx.author)

    lower = float(arg1.strip())
    upper = float(arg2.strip())

    if lower >= upper:
        upper = float(arg1.strip())
        lower = float(arg2.strip())

    else:
        pass

    if "hour" in choice.content:

        rss_address = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
        json_data = requests.get(rss_address).json()

        totalcount = json_data['metadata']['count']

        Number = []
        magnv = []
        for i in range(totalcount):

            magn = json_data['features'][i]['properties']['mag']
            if  upper >= magn >= lower:
                Number.append(json_data['features'][i]['properties']['place'])
                magnv.append(magn)   #location

        if len(Number) >= 1:
            for i in range(totalcount):
                await ctx.send(f'``{Number[i]}\n``')
        else:
            await ctx.send("Sorry, there were none reported in the past hour")


    if "day" in choice.content:

        rss_address = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
        json_data = requests.get(rss_address).json()

        totalcount = json_data['metadata']['count']
        lower = float(arg1.strip())
        upper = float(arg2.strip())

        if lower >= upper:
            upper = float(arg1.strip())
            lower = float(arg2.strip())

        else:
            pass
        Number = []
        magnv = []
        for i in range(totalcount):

            magn = json_data['features'][i]['properties']['mag']
            if upper>=magn >= lower:
                Number.append(json_data['features'][i]['properties']['place'])
                magnv.append(magn)  #location

        if len(Number) >= 1:
            for i in range(totalcount):
                if len(Number)<= 60:
                    await ctx.send(f'``{Number[i]}:{magnv[i]}\n``')
                else:
                    await ctx.send("Nu")
                    return
        else:
            await ctx.send("Sorry, there were none reported in the past day")


    if "month" in choice.content:

        rss_address = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"
        json_data = requests.get(rss_address).json()

        totalcount = json_data['metadata']['count']
        lower = float(arg1.strip())
        upper = float(arg2.strip())

        if lower >= upper:
            upper = float(arg1.strip())
            lower = float(arg2.strip())

        else:
            pass
        Number = []
        magnv = []
        for i in range(totalcount):

            magn = json_data['features'][i]['properties']['mag']
            if upper>=magn >= lower:
                Number.append(json_data['features'][i]['properties']['place'])
                magnv.append(magn)  #location

        if len(Number) >= 1:
            for i in range(totalcount):
                if len(Number)<= 60:
                    await ctx.send(f'``{Number[i]}:{magnv[i]}\n``')
                else:
                    await ctx.send("Nu")
                    await ctx.send("OK FINE. But I will only show you a peak UwU")
                    for j in range(10):
                        await ctx.send(f'``{Number[j]}:{magnv[j]}\n``')
                    return
        else:
            await ctx.send("Sorry, there were none reported in the past day")

