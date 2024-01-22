import g4f

g4f.debug.logging = True  # Enable logging
g4f.check_version = False  # Disable automatic version checking
print(g4f.version)  # Check version
print(g4f.Provider.Ails.params)  # Supported args

response = g4f.ChatCompletion.create(
    provider=g4f.Provider.Phind,
    model=g4f.models.gpt_35_turbo,
    messages=[
        {
            "role": "user",
            "content": "Hello!",
        }
    ],
    stream=False,
)

print(response)
