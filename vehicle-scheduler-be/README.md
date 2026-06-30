## Vehicle Scheduler Backend
1. In postman below Body open raw and JSON editor 
2. Authorization 
Auth Type - Bearer Token
Token - (given token)
3. Method ['GET']
4. SEND
5. {} JSON output as:
{
    "depots": [
        {
            "ID": 2,
            "MechanicHours": 135
        },
        {
            "ID": 3,
            "MechanicHours": 188
        },
        {
            "ID": 4,
            "MechanicHours": 97
        },
        {
            "ID": 5,
            "MechanicHours": 164
        }
    ]
}
6. json response 2:
{
    "vehicles": [
        {
            "TaskID": "241fd0cb-ca2a-4f7f-9f2f-9e4d7303bc97",
            "Duration": 7,
            "Impact": 4
        },
        {
            "TaskID": "aef741df-a4e0-4782-9a01-be98306f7b38",
            "Duration": 4,
            "Impact": 8
        },
        {
            "TaskID": "e8178e35-010f-44aa-a698-e8f430b8fb23",
            "Duration": 4,
            "Impact": 9
        },
        {
            "TaskID": "75ec175a-0ac6-48d0-87d5-ad531efb2a1e",
            "Duration": 8,
            "Impact": 1
        },
        {
            "TaskID": "8f8f2129-2a4c-4ea3-ae0d-1c76ade442d4",
            "Duration": 1,
            "Impact": 3
        },
        {
            "TaskID": "a0f18a1a-d88b-47bd-bce6-bfde7928c934",
            "Duration": 1,
            "Impact": 5
        },
        {
            "TaskID": "e888cb0e-f2ec-4752-8786-a73ead4a0acc",
            "Duration": 3,
            "Impact": 7
        },
        {
            "TaskID": "26576391-1fba-4b43-962d-17575580b629",
            "Duration": 1,
            "Impact": 1
        },
        {
            "TaskID": "7a205032-cd62-4b22-b650-4c2eab3b4da2",
            "Duration": 5,
            "Impact": 10
        },
        {
            "TaskID": "800863e5-8761-4ba1-bcd9-692f438307ca",
            "Duration": 7,
            "Impact": 7
        },
        {
            "TaskID": "e8f5e143-888f-4066-a238-9a00e01ca9d8",
            "Duration": 2,
            "Impact": 3
        },
        {
            "TaskID": "575e9ad2-a83b-4c48-b3b3-697700ba88f7",
            "Duration": 2,
            "Impact": 5
        },
        {
            "TaskID": "7613db01-a318-4505-abec-7cf9919680b6",
            "Duration": 7,
            "Impact": 3
        },
        {
            "TaskID": "9878b6b3-3897-4de6-b69b-4a73e846aae8",
            "Duration": 7,
            "Impact": 2
        },
        {
            "TaskID": "9c9bfcf3-75df-434d-9d9c-98d58dad9926",
            "Duration": 4,
            "Impact": 3
        },
        {
            "TaskID": "de572d03-bb88-4640-89ef-c88d2438b503",
            "Duration": 1,
            "Impact": 1
        },
        {
            "TaskID": "7386a2d0-a52c-4323-b9f1-ca143ca6bd58",
            "Duration": 5,
            "Impact": 2
        },
        {
            "TaskID": "6992a6fd-5852-45ee-a43f-1b3ec7dfe047",
            "Duration": 7,
            "Impact": 3
        },
        {
            "TaskID": "c4171b35-d73b-4d9b-a674-4034a3103428",
            "Duration": 5,
            "Impact": 6
        },
        {
            "TaskID": "47e26b2f-339a-42ac-ada3-2c9cae8ec592",
            "Duration": 5,
            "Impact": 1
        },
        {
            "TaskID": "21abbbbf-a128-48b9-9dbc-3e11965030fc",
            "Duration": 6,
            "Impact": 8
        },
        {
            "TaskID": "b0e4d207-3c7a-4d5a-a2d5-ee36f62b8f2a",
            "Duration": 8,
            "Impact": 9
        },
        {
            "TaskID": "ddf6966b-839c-4c6b-9387-d093e340b77d",
            "Duration": 3,
            "Impact": 3
        },
        {
            "TaskID": "61414924-e180-488a-9ea2-4f33e1ddeea4",
            "Duration": 4,
            "Impact": 4
        },
        {
            "TaskID": "b60dc9a1-2d7a-40e2-b1fd-556092a48f18",
            "Duration": 1,
            "Impact": 1
        },
        {
            "TaskID": "e9860286-763d-4294-a21f-04e23150dcf2",
            "Duration": 7,
            "Impact": 7
        },
        {
            "TaskID": "6b3230c9-9a94-40c5-9b24-1115c62604e4",
            "Duration": 1,
            "Impact": 5
        },
        {
            "TaskID": "eeb86983-7256-4747-a334-61dab4e29355",
            "Duration": 1,
            "Impact": 5
        },
        {
            "TaskID": "23e8213f-0f20-4dd0-9185-c8df11266ba9",
            "Duration": 4,
            "Impact": 2
        },
        {
            "TaskID": "da2ebe7a-1352-490d-95c1-2807c7926f21",
            "Duration": 3,
            "Impact": 3
        },
        {
            "TaskID": "2f03359d-ab4f-4591-ac1c-fa33d77d92a3",
            "Duration": 2,
            "Impact": 5
        },
        {
            "TaskID": "39a6c93d-4451-4093-9a0c-0a63adf744d1",
            "Duration": 4,
            "Impact": 2
        },
        {
            "TaskID": "368baafc-c7fd-4eb8-8d55-04cb1fa523c8",
            "Duration": 5,
            "Impact": 6
        },
        {
            "TaskID": "c85b2590-7d9e-474b-8795-3ae63296a2b6",
            "Duration": 3,
            "Impact": 7
        },
        {
            "TaskID": "3d7034e6-286b-47cb-aeb9-05d75e4959fd",
            "Duration": 1,
            "Impact": 5
        },
        {
            "TaskID": "2d221c97-85d6-4b8e-b182-f871d47035f0",
            "Duration": 7,
            "Impact": 1
        },
        {
            "TaskID": "04549b27-032e-4cf1-90f3-0d6064b46362",
            "Duration": 5,
            "Impact": 3
        },
        {
            "TaskID": "45ae0eff-dc9c-4a4f-83d7-9ace2b45e665",
            "Duration": 3,
            "Impact": 6
        },
        {
            "TaskID": "6990e508-bc77-4555-b17b-44b94e322e6a",
            "Duration": 3,
            "Impact": 9
        },
        {
            "TaskID": "5ca72fbb-fc68-4e40-8c35-eae28d2921b3",
            "Duration": 1,
            "Impact": 4
        }
    ]
}