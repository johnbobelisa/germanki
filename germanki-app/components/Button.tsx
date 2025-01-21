// components/Button.tsx
import { StyleSheet, View, Pressable, Text, ViewStyle } from 'react-native';

type Props = {
  label: string;
  onPress?: () => void;
  style?: ViewStyle; // New prop to allow custom styles
};

export default function Button({ label, onPress, style }: Props) {
  return (
    <View style={styles.buttonContainer}>
      <Pressable 
        style={[styles.button, style]} // Merge default styles with custom styles
        onPress={onPress || (() => alert('You pressed a button.'))}
      >
        <Text style={styles.buttonLabel}>{label}</Text>
      </Pressable>
    </View>
  );
}

const styles = StyleSheet.create({
  buttonContainer: {
    width: 320,
    height: 68,
    marginHorizontal: 20,
    alignItems: 'center',
    justifyContent: 'center',
    padding: 3,
  },
  button: {
    borderRadius: 10,
    width: '100%',
    height: '100%',
    alignItems: 'center',
    justifyContent: 'center',
    flexDirection: 'row',
    backgroundColor: '#007BFF', // Default background color
  },
  buttonLabel: {
    color: '#fff', // Default text color
    fontSize: 16,
  },
});
