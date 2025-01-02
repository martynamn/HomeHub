import base64
import json
import uuid
from datetime import datetime

from django.http import JsonResponse
from pymongo import MongoClient

from myapp.models import User
from myapp.serializer import UserSerializer
from myproject import settings

client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
db = client[settings.DATABASES['default']['NAME']]


def create_user(metadata, files):
    try:
        user_data = create_user_record(metadata, files)
        db.USER.insert_one(user_data)

        return JsonResponse({'message': 'User created successfully'}, status=201)

    except Exception as e:
        print(e)
        return JsonResponse({'error': f'Error occurred creating user, {e}'}, status=400)


def get_users():
    users = User.objects.all()
    users_premium = [user for user in users if user.premium == True]

    if not users:
        return JsonResponse({'error': 'No users with premium subscription found'}, status=404)

    users_list = UserSerializer(users_premium, many=True).data
    return JsonResponse(users_list, safe=False)


def get_user(user_id: str):
    user = User.objects.get(_id=user_id)

    if not user:
        return JsonResponse({'error': 'No user found'}, status=404)

    users_list = UserSerializer(user).data
    return JsonResponse(users_list, safe=False)


def update_user(metadata, files, user_id: str):
    try:
        user = create_user_record(metadata, files)
        result = db.USER.find_one_and_update(
            {'_id': user_id},
            {'$set': user},
            return_document=True
        )
        if result is None:
            return JsonResponse({'error': 'User not found'}, status=404)

        return JsonResponse({'success': True, 'message': 'User updated successfully'})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def set_subscription(user_id: str):
    try:
        result = db.USER.find_one_and_update(
            {'_id': user_id},
            {'$set': {"premium": True}},
            return_document=True
        )
        if result is None:
            return JsonResponse({'error': 'User not found'}, status=404)

        return JsonResponse({'success': True, 'message': 'User updated successfully'})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def delete_user(user_id: str):
    try:
        result = db.USER.delete_one({'_id': user_id})

        if result.deleted_count == 0:
            return JsonResponse({'User not found'}, status=404)
        return JsonResponse({'success': True, 'message': 'Usery deleted successfully'})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def create_user_record(metadata, files):
    data = json.loads(metadata)
    image_ids = []
    for file in files:
        file_content = file.read()
        encoded_image = base64.b64encode(file_content).decode('utf-8')

        image_id = str(uuid.uuid4())

        image_data = {
            '_id': image_id,
            'imageData': encoded_image,
            'filename': file.name,
            'uploadDate': datetime.now()
        }

        db.IMAGE.insert_one(image_data)
        image_ids.append(image_id)
    user_data = {
        '_id': data.get('userId'),
        'firstName': data.get('firstName'),
        'lastName': data.get('lastName'),
        'phone': data.get('phone'),
        'gender': data.get('gender'),
        'email': data.get('email'),
        'country': data.get('country'),
        'city': data.get('city'),
        'description': data.get('description'),
        'agencyName': data.get('agencyName'),
        'AgentLicenseId': data.get('AgentLicenseId'),
        'premium': data.get('premium'),
        'images': image_ids
    }
    return user_data
