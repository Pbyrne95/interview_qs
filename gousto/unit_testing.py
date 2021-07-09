import unittest
import read_json as rd


instance = rd.calc_demension_class()

## add edge cases 
class testStamp(unittest.TestCase):
    # def test_result(self):
    #     self.assertEqual(rd.get_json_data("test.json"),{'data':'test'})
       
    # def test_type(self):
    #     self.assertEqual(type(rd.get_json_data("test.json")),dict)

    def test_area(self):
        self.assertEqual(instance.calc_box_volume(20,100,50),100_000/1000)
        self.assertEqual(instance.calc_box_volume(20,80,50),80_000/1000)
        self.assertEqual(instance.calc_box_volume(30,50,60),90_000/1000)  
    
if __name__ == "__main__":
    unittest.main()