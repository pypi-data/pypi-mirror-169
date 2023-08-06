from rest_framework import serializers

from base_pack.finflo.transition import FinFlotransition
from .models import TransitionManager , workevents , workflowitems , Action
from django.conf import settings
from django.apps import apps




class Workeventsserializer(serializers.ModelSerializer):
    from_party = serializers.SlugRelatedField(read_only=True,slug_field = "description")
    to_party = serializers.SlugRelatedField(read_only=True,slug_field = "description")
    class Meta:
        model = workevents
        fields = [
            'id',
            'action',
            'subaction',
            'initial_state',
            'interim_state',
            'final_state',
            'event_user',
            'record_datas',
            'from_party',
            'to_party',
            'final_value'
        ]





class Workitemserializer(serializers.ModelSerializer):
    WorkFlowEvents = Workeventsserializer(many=True, read_only=True)
    current_from_party = serializers.SlugRelatedField(read_only=True,slug_field = "description")
    current_to_party = serializers.SlugRelatedField(read_only=True,slug_field = "description")
    record_datas = serializers.SerializerMethodField()

    class Meta:
        model = workflowitems
        fields = [
            'id',
            'transitionmanager',
            'initial_state',
            'interim_state',
            'final_state',
            'event_user',
            'action',
            'subaction',
            'record_datas',
            'next_available_transitions',
            'current_from_party',
            'current_to_party',
            'WorkFlowEvents',
        ]
    
    def get_record_datas(self,obj):
        t_id , type = obj.transitionmanager.t_id , obj.transitionmanager.type
        gets_transition = FinFlotransition(t_id = t_id , type = type , action  = None,interim = None , source = None , target = None)
        return gets_transition.get_record_datas()




class TransitionManagerserializer(serializers.ModelSerializer):
    workflowitems = Workitemserializer(read_only = True)
    model = serializers.SerializerMethodField()
    wf_item_id = serializers.SerializerMethodField()
    class Meta:
        model = TransitionManager
        fields = [
            'id',
            'type',
            't_id',
            'wf_item_id',
            'model',
            'workflowitems'
        ]

    def get_model(self,obj):
        try:
            arr = settings.FINFLO['WORK_MODEL']
            for i in arr:
                user = apps.get_model(i)
                qs = user.objects.filter(id = obj.t_id ).values()
                if qs.exists():
                    break
            return qs
        except:
            return None
                    

    def get_wf_item_id(self,obj):
        return obj.workflowitems.id



class Actionseriaizer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = '__all__'



class workflowitemslistserializer(serializers.ModelSerializer):
    class Meta:
        model = workflowitems
        fields = '__all__'


class workeventslistserializer(serializers.ModelSerializer):
    class Meta:
        model = workevents
        fields = '__all__'




