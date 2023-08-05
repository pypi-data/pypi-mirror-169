# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bfportal_grpc', 'bfportal_grpc.proto']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0', 'grpcio==1.48.1', 'protobuf==4.21.6']

setup_kwargs = {
    'name': 'bfportal-grpc',
    'version': '0.1.3',
    'description': ' bf2042 portal web grpc as python package ',
    'long_description': '# Battlefield Portal web-grpc\n\nThis npm package can be used to directly call the https://portal.battlefield.com/ api.\nwe\'re making this public since you can read the javascript of the website and figure this out yourself easily anyway, but we want to make sure only 1 github repo has to be kept in sync with the api and the rest that uses it just has to update a package and a few code changes to still have it work.\n\nhttps://www.npmjs.com/package/bfportal-grpc\n\n## example\n\n```js\nimport { CommunityGamesClient, communitygames } from \'bfportal-grpc\';\n\nconst communityGames = new CommunityGamesClient(\'https://kingston-prod-wgw-envoy.ops.dice.se\', null);\nconst metadata = {\n    \'x-dice-tenancy\': \'prod_default-prod_default-kingston-common\',\n    \'x-gateway-session-id\': sessionId,\n    \'x-grpc-web\': \'1\',\n    \'x-user-agent\': \'grpc-web-javascript/0.1\',\n}\n\nconst request = new communitygames.GetPlaygroundRequest();\nrequest.setPlaygroundid(testPlayground);\nconst response = await communityGames.getPlayground(request, metadata);\nconst modRules = response.getPlayground()?.getOriginalplayground()?.getModrules()?.getCompatiblerules()?.getRules();\nif (modRules instanceof Uint8Array) {\n    console.log(new TextDecoder().decode(modRules))\n}\nconst playgroundName = response.getPlayground()?.getOriginalplayground()?.getName();\n```\n\nthe proto files are accessable directly via "node_modules/bfportal-grpc/proto/communitygames.proto" to for example decode to json:\n```js\n// use reponse from previous example\nconst root = await load("node_modules/bfportal-grpc/proto/communitygames.proto");\nconst AwesomeMessage = root.lookupType("web.communitygames.PlaygroundInfoResponse");\nconst decoded = AwesomeMessage.decode(response.serializeBinary());\nconst json_str = JSON.stringify(decoded, null, 4);\n```\n\n### non-async example\n\n```js\nimport { CommunityGamesClient, communitygames } from \'bfportal-grpc\';\n\nconst communityGames = new CommunityGamesClient(\'https://kingston-prod-wgw-envoy.ops.dice.se\', null);\nconst metadata = {\n    \'x-dice-tenancy\': \'prod_default-prod_default-kingston-common\',\n    \'x-gateway-session-id\': sessionId,\n    \'x-grpc-web\': \'1\',\n    \'x-user-agent\': \'grpc-web-javascript/0.1\',\n}\n\nconst request = new communitygames.GetPlaygroundRequest();\nrequest.setPlaygroundid("bbe433c0-13fa-11ed-bc32-24a8c2c0764e");\nconst call = communityGames.getPlayground(request, metadata,\n  (_err: grpcWeb.Error, response: communitygames.PlaygroundInfoResponse) => {\n    // console.log("err:", _err)\n    var modRules = response.getPlayground()?.getOriginalplayground()?.getModrules()?.getCompatiblerules()?.getRules();\n    if (modRules instanceof Uint8Array) {\n        console.log(new TextDecoder().decode(modRules))\n    }\n\n    load("node_modules/bfportal-grpc/proto/communitygames.proto", function(err, root) {\n      if (err)\n        throw err;\n      if (root == undefined) \n        return\n\n      const AwesomeMessage = root.lookupType("web.communitygames.PlaygroundInfoResponse");\n\n      let decoded = AwesomeMessage.decode(response.serializeBinary());\n      fs.writeFile("test.json", JSON.stringify(decoded, null, 4), function(err: any) {\n        if (err) {\n            console.log(err);\n        }\n      });\n    })\n});\n```\n\n## python\nfor python you can use the \'sonora\' package to do grpc-web\n```py\nimport sonora.aio\nimport sys\nfrom proto import communitygames_pb2, communitygames_pb2_grpc\n\nasync def main():\n    async with sonora.aio.insecure_web_channel(\n        f"https://kingston-prod-wgw-envoy.ops.dice.se"\n    ) as channel:\n        stub = communitygames_pb2_grpc.CommunityGamesStub(channel)\n        response: communitygames_pb2.PlaygroundInfoResponse = await stub.getPlayground(communitygames_pb2.GetPlaygroundRequest(playgroundId="10992a10-461a-11ec-8de0-d9f491f92236"), metadata=(\n            (\'x-dice-tenancy\', \'prod_default-prod_default-kingston-common\'),\n            (\'x-gateway-session-id\', \'web-c6b312c9-2520-4fde-958d-60ae71840a65\'),\n            (\'x-grpc-web\', \'1\'),\n            (\'x-user-agent\', \'grpc-web-javascript/0.1\')\n        ))\n```\n\n### current build method from proto to javascript via python\nneeds proto-compile, which can be installed with:\n`pip3 install proto-compile`\n\nand build with:\n`proto-compile --clear-output-dirs --verbosity=1 ./proto ./src/proto grpc-web --grpc_web_out_options="import_style=typescript,mode=grpcweb"`\n\nbuilding for python requires grpcio-tools, which can be installed with:\n`pip3 install grpcio-tools`\n\nand build with:\n`python3 -m grpc_tools.protoc -I. --python_out=./grpc-python --grpc_python_out=./grpc-python ./proto/communitygames.proto ./proto/localization.proto ./proto/authentication.proto ./proto/reporting.proto`\n\npython package used: https://github.com/romnn/proto-compile\n\n### Pushing your changes\npackage versions can be made with `npm run build` and `npm version patch` `git push --tags origin main` to release.\nfor python patch with `npm run build:python`, `npm run python:setimports` and `poetry build`.\n\nexample library used: https://github.com/tomchen/example-typescript-package\n',
    'author': 'iiTzArcur',
    'author_email': 'arcur@gametools.network',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/community-network/bfportal-grpc',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
