// app/(tabs)/index.tsx
import { View, Text, StyleSheet } from 'react-native';
import { Redirect } from 'expo-router';
import Button from '@/components/Button';
import { router } from 'expo-router';

export default function Tab() {
  const isAuthenticated = global.localStorage.getItem('isAuthenticated') === 'true';

  if (!isAuthenticated) {
    return <Redirect href="/login" />;
  }

  return (
    <View style={styles.container}>
      <Button 
        label="Sign Out" 
        onPress={() => {
          // Remove the auth flag
          global.localStorage.removeItem('isAuthenticated');
          // Navigate back to login
          router.replace('/login');
        }}
        style={{ backgroundColor: 'black' }}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});
