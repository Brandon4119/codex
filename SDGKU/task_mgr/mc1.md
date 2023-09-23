# Mini Challenge 1

## Create additional tooling for update and delete

### Acceptance Criteria

1. Create a utility/tool script for updating tasks.
   1.1. As a bonus step, display the task prior to it being updated.
   1.2. As an additional bonus step, display the task after it was updated.
2. Create a utility/tool script for deleting tasks.
   2.1. As an additional step, display the task that is to be deleted and request confirmation.

### Note

The `requests` function to issue put requests is `put`.
The `requests` function to issue delete requests is `delete`.

Example:

```
rsp = requests.put(URL, json=something)
...
rsp = requests.delete(URL)
```
