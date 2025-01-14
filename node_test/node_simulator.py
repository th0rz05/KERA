import asyncio
import json
import logging

HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 18019  # Port to listen on

# Set up logging
logging.basicConfig(level=logging.INFO)

async def read_messages(reader, writer):
    while True:
        data = await reader.read(1024)  # Read up to 100 bytes
        if not data:
            logging.info("Connection closed by client.")
            
            # Close the TCP port
            writer.close()
            await writer.wait_closed()
            
            break

        # The incoming data might contain multiple messages
        messages = data.decode('utf-8').split("\n")
        for message in messages:
            if message.strip():  # Ignore empty lines
                logging.info(f"\n\nReceived message: {message}\n\n")
                # Process the received message as JSON
                try:
                    msg_dict = json.loads(message)
                    # logging.info(f"Parsed JSON: {msg_dict}")
                except json.JSONDecodeError:
                    logging.error("Received an invalid JSON message.")

async def async_input(prompt: str) -> str:
    """Asynchronous wrapper for input using a thread to avoid blocking the event loop."""
    return await asyncio.to_thread(input, prompt)

async def send_messages(writer):
    while True:
        print("Choose a response to send back:")
        
        # Use async_input to avoid blocking the event loop
        choice = await async_input("Enter number: ")

        if choice == "1":
            response = {
                "type": "hello",
                "version": "0.10.0",
                "agent": "Kerma Agent 47"
            }
        elif choice == "2":
            response = {
                "type": "getmempool",
            }
        elif choice == "3":
            response = {
                "type": "mempool",
                "txids": ["e565db393706f79608dfb0e1f7129ae0765b5e3b08e89cf868098b27af49e187"]
            }
        elif choice == "4":
            response = {
                "type": "getobject",
                "objectid": "d46d09138f0251edc32e28f1a744cb0b7286850e4c9c777d7e3c6e459b289347"  # Example object ID
            }
        elif choice == "5":
            response = {
                "type": "ihaveobject",
                "objectid": "0000000052a0e645eca917ae1c196e0d0a4fb756747f29ef52594d68484bb333"  # Example object ID
            }
        elif choice == "6":
            #7e979209c75dc66af139f19de26e651eac541b6b5d5803fde6ee00fda1a7d0ca
            # tiago - coinbase transaction
            response = {
                "type": "object",
                "object": {
                        "type": "transaction",
                        "height": 1,
                        "outputs": [
                            {
                                "pubkey": "da550c7ac3d73fa6b13e8a04b7c5ab59c13119ee2a22a2849164235a008fbfbb",
                                "value": 50
                            }
                        ]
                    },
            }
        elif choice == "7":
            #00003382e1df39a15b8df27fa93f0c98424a7a387964d8df1bb11f81b96ce949
            #block 1
            response = {"object":
                {
                    "type": "block",
                    "txids": [
                        "7e979209c75dc66af139f19de26e651eac541b6b5d5803fde6ee00fda1a7d0ca"
                    ],
                    "nonce": "0000000000000000000000000000000000000000000000000000000000018dce",
                    "previd": "00002fa163c7dab0991544424b9fd302bb1782b185e5a3bbdf12afb758e57dee",
                    "created": 1736812201,
                    "T": "0000abc000000000000000000000000000000000000000000000000000000000",
                    "miner": "block 1",
                    "note": "Mined block"
                }
                ,"type":"object"}
        elif choice == "8":
            #efca8dda6c5170a0dafd11419ec8624133f68232381939840b060ed4756f5603
            # 10 to john 40 to tiago
            response = {
                "type": "object",
                "object": {
                    "type": "transaction",
                    "inputs": [
                        {
                            "outpoint": {
                                "txid": "7e979209c75dc66af139f19de26e651eac541b6b5d5803fde6ee00fda1a7d0ca",
                                "index": 0
                            },
                            "sig": "de2c6f418b81733bd7d073a8dbe903e37581890273cb0d74427ef0b88a1fb716dbffebb516c11f1bfefeae7e2a9019b019adc8f0c939fbfb5249a7994c375e07"
                        }
                    ],
                    "outputs": [
                        {
                            "pubkey": "3391602a43aeb4ae9140f969240e955bf2b0833f325a1a12726cee5d4cda7ed5",
                            "value": 10
                        },
                        {
                            "pubkey": "da550c7ac3d73fa6b13e8a04b7c5ab59c13119ee2a22a2849164235a008fbfbb",
                            "value": 40
                        }
                    ]
                }
            }
        elif choice == "9":
            #e565db393706f79608dfb0e1f7129ae0765b5e3b08e89cf868098b27af49e187
            # 5 to john 5 to alice
            response = {
                "type": "object",
                "object": {
                    "type": "transaction",
                    "inputs": [
                        {
                            "outpoint": {
                                "txid": "efca8dda6c5170a0dafd11419ec8624133f68232381939840b060ed4756f5603",
                                "index": 0
                            },
                            "sig": "2265e0b94604ffea28df418ca5b8c606f60859d978291ea38e3eac56bfd58fb0a863a5469ef2104b59b8ef5508f4ffbd3f862f44847458cd9037fbec9f8c7804"
                        }
                    ],
                    "outputs": [
                        {
                            "pubkey": "3391602a43aeb4ae9140f969240e955bf2b0833f325a1a12726cee5d4cda7ed5",
                            "value": 5
                        },
                        {
                            "pubkey": "921c38b1f83f2ca0aae021239aabe22916e512f0800940420bf3ffd10da64575",
                            "value": 5
                        }
                    ]
                }
            }
        elif choice == "10":
            #0000a35d59c48f607fd2ed705dec11e54851c962afbf380e529413ba86212876
            #block 2
            response = {
                "type": "object",
                "object": {
                    "type": "block",
                    "txids": [
                        "efca8dda6c5170a0dafd11419ec8624133f68232381939840b060ed4756f5603"
                    ],
                    "nonce": "000000000000000000000000000000000000000000000000000000000000d1eb",
                    "previd": "00003382e1df39a15b8df27fa93f0c98424a7a387964d8df1bb11f81b96ce949",
                    "created": 1736870448,
                    "T": "0000abc000000000000000000000000000000000000000000000000000000000",
                    "miner": "block 2",
                    "note": "Mined block"
                }
            }
        elif choice == "11":
            #b8ef58a7cf286db762a515717bce5bdfd2e0a7f6168ddc77ea88cfb5149ac5c9
            #coinbase transaction 50 to alice
            response = {
                "type": "object",
                "object": {
                    "type": "transaction",
                    "height": 2,
                    "outputs": [
                        {
                            "pubkey": "921c38b1f83f2ca0aae021239aabe22916e512f0800940420bf3ffd10da64575",
                            "value": 50
                        }
                    ]
                }
            }
        elif choice == "12":
            #00007017eff3474123df6db702b06a97f56137bcf66c0ddc627039b3253079ad
            #block 2 slash
            response = {
                "type": "object",
                "object": {
                    "type": "block",
                    "txids": [
                        "b8ef58a7cf286db762a515717bce5bdfd2e0a7f6168ddc77ea88cfb5149ac5c9"
                    ],
                    "nonce": "0000000000000000000000000000000000000000000000000000000000004793",
                    "previd": "00003382e1df39a15b8df27fa93f0c98424a7a387964d8df1bb11f81b96ce949",
                    "created": 1736876241,
                    "T": "0000abc000000000000000000000000000000000000000000000000000000000",
                    "miner": "block 2 slash",
                    "note": "Mined block"
                }
            }      
        elif choice == "13":
            #fbe02d5aa534faef8e614143b01ffb0fb780e1520bae16141de061cba353c751
            #alice pays 10 to tiago and 40 to herself
            response = {
                "type": "object",
                "object": {
                    "type": "transaction",
                    "inputs": [
                        {
                            "outpoint": {
                                "txid": "b8ef58a7cf286db762a515717bce5bdfd2e0a7f6168ddc77ea88cfb5149ac5c9",
                                "index": 0
                            },
                            "sig": "02e6b4807fb7dd85b3e5d3793bc32164921a2850a48e2024a3f0d5709b08c9a4f19491cc5b8b0473fdeac1b01b64337d0d7f22959326f2696daa5657f729ef00"
                        }
                    ],
                    "outputs": [
                        {
                            "pubkey": "da550c7ac3d73fa6b13e8a04b7c5ab59c13119ee2a22a2849164235a008fbfbb",
                            "value": 10
                        },
                        {
                            "pubkey": "921c38b1f83f2ca0aae021239aabe22916e512f0800940420bf3ffd10da64575",
                            "value": 40
                        }
                    ]
                }
            }
        elif choice == "14":
            #00007e5514b00d54d9464965d752e227af7f9daf8118a34c35e1a33502cd7500
            #block 3 slash
            response = {
                "type": "object",
                "object": {
                    "type": "block",
                    "txids": [
                        "fbe02d5aa534faef8e614143b01ffb0fb780e1520bae16141de061cba353c751"
                    ],
                    "nonce": "0000000000000000000000000000000000000000000000000000000000009c19",
                    "previd": "00007017eff3474123df6db702b06a97f56137bcf66c0ddc627039b3253079ad",
                    "created": 1736877608,
                    "T": "0000abc000000000000000000000000000000000000000000000000000000000",
                    "miner": "block 3 slash",
                    "note": "Mined block"
                }
            }
        else:
            print("Invalid choice.")
            continue

        # Send the response to the server
        writer.write((json.dumps(response) + "\n").encode('utf-8'))
        await writer.drain()
        print(f"Sent response: {json.dumps(response)}")

async def handle_client(reader, writer):
    # Run both reading and sending tasks in parallel
    read_task = asyncio.create_task(read_messages(reader,writer))
    send_task = asyncio.create_task(send_messages(writer))

    # Wait for both tasks to finish (they will run indefinitely until the connection closes)
    await asyncio.gather(read_task, send_task)

    logging.info("Closing the connection.")
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(handle_client, HOST, PORT)
    logging.info(f'Serving on {HOST}:{PORT}')

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Server shutting down.")
