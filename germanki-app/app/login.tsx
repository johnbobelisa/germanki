// app/login.tsx
import { Text, View, StyleSheet } from 'react-native';
import { Link, router } from 'expo-router';
import Button from '@/components/Button';

export default function LoginScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.text}>Login screen</Text>
      <Button 
        label="Temporarily authenticate yourself" 
        onPress={() => {
          // Set a temporary flag in localStorage
          global.localStorage.setItem('isAuthenticated', 'true');
          // Navigate to tabs
          router.replace('/(tabs)');
        }}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#25292e',
    justifyContent: 'center',
    alignItems: 'center',
  },
  text: {
    color: '#fff',
  },
  button: {
    fontSize: 20,
    textDecorationLine: 'underline',
    color: '#fff',
  },
});
