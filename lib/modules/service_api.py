from api_core.req import Session
from data.config import HOST


class ServiceApi(Session):
    create_entity_url = HOST + "/api/create"
    get_entities_url = HOST + "/api/getAll"
    get_entity_url = HOST + "/api/get/{}"
    delete_entity_url = HOST + "/api/delete/{}"
    update_entity_url = HOST + "/api/patch/{}"

    def sa_create_entity(self, **kwargs):
        return self.post(url=self.create_entity_url, **kwargs)

    def sa_get_all_entities(self):
        return self.get(url=self.get_entities_url)

    def sa_get_entity(self, entity_id):
        return self.get(url=self.get_entity_url.format(entity_id))

    def sa_delete_entity(self, entity_id):
        return self.delete(url=self.delete_entity_url.format(entity_id))

    def sa_update_entity(self, entity_id, **kwargs):
        return self.patch(url=self.update_entity_url.format(entity_id), **kwargs)
